# ЛР5 — JSON и конвертации (JSON↔CSV, CSV→XLSX): Техническое задание
## Задание A

### функция json_to_csv
```python
def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if json_file.suffix.lower() != ".json":
         raise ValueError('исходный файл должен иметь расширение .json')

    if csv_file.suffix.lower() != ".csv":
         raise ValueError('результирующий файл должен иметь расширение .csv')

    if not json_file.exists():
         raise FileNotFoundError('файл отсутствует')

    with json_file.open("r", encoding="utf-8") as jf:
        try:
             data = json.load(jf)
        except json.JSONDecodeError:
             raise ValueError('пустой JSON-файл или неподдерживаемая структура')
    
    if not isinstance(data,list) or len(data)==0:
         raise ValueError('JSON-файл пуст или имеет неверный формат')
    
    ensure_parent_dir(csv_file)

    fieldnames = list(data[0].keys())

    with csv_file.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames)
        w.writeheader()
        w.writerows(data)
```
1. Проверяет существование входного файла
2. Проверяет расширение .json и .csv
3. Читает JSON в кодировке UTF-8
4. Проверяет, что корневой объект является непустым списком словарей
5. Собирает названия всех ключей в порядке их первого появления
6. Записывает заголовок и строки в CSV в кодировке UTF-8; если отсутствует 
значение для одного из заголовков, соответствующая ячейка CSV остаётся пустой.

### Тест-кейс

```python
json_to_csv(r'data/lab05/samples/people.json', r'data/lab05/out/people_from_json.csv')
```
<img width="347" height="612" alt="img1_1" src="https://github.com/user-attachments/assets/779044d3-9706-497e-9942-0df1d237cd18" /> 
<img width="351" height="168" alt="img1_2" src="https://github.com/user-attachments/assets/7b86a220-3f76-4cb3-b4ec-f3d3c628f81a" />

### Свой пример

```python
json_to_csv(r'data/lab05/samples/phones.json', r'data/lab05/out/phones_from_json.csv')
```
<img width="347" height="395" alt="img1_3" src="https://github.com/user-attachments/assets/86b77a82-30b6-4360-8b35-de222e47b696" />
<img width="358" height="119" alt="img1_4" src="https://github.com/user-attachments/assets/246881df-a399-4ecf-b5ee-c9cd0463d34d" />

### функция csv_to_json

```python
def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if csv_file.suffix.lower() != ".csv":
         raise ValueError('входной файл должен иметь расширение .csv')
    
    if json_file.suffix.lower() != ".json":
         raise ValueError('выходной файл должен иметь расширение .json')
    
    if not csv_file.exists():
         raise FileNotFoundError('файл отсутствует')

    with csv_file.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV не содержит заголовок")
        
        data = list(reader)
        if not data:
            raise ValueError("CSV-файл пуст или не содержит строк с данными")

    ensure_parent_dir(json_file)

    with json_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
```

1. Проверяет существование входного файла
2. Проверяет расширение .csv и .json
3. Читает CSV в кодировке UTF-8
4. Проверяет наличие заголовка и хотя бы одной строки данных
5. Преобразует каждую строку в словарь
6. Сохраняет список словарей в JSON с отступом в два пробела

### Тест-кейс

```python
csv_to_json(r'data/lab05/samples/people.csv', r'data/lab05/out/people_from_csv.json')
csv_to_json(r'data/lab05/samples/cities.csv', r'data/lab05/out/cities.json')
```
<img width="306" height="158" alt="img2_1" src="https://github.com/user-attachments/assets/2c46bfc1-8b82-49b6-a609-42897dc34270" /> <img width="384" height="615" alt="img2_2" src="https://github.com/user-attachments/assets/dd396fa5-3f25-4a55-8cbb-ffe3a7609e9e" />

<img width="323" height="157" alt="img2_3" src="https://github.com/user-attachments/assets/f6b44261-f74f-4bf2-94da-a6887a70976e" /> <img width="331" height="613" alt="img2_4" src="https://github.com/user-attachments/assets/3ee02ebe-8c49-4902-b530-6e00228c8c4f" />


### Свой пример

```python
csv_to_json(r'data/lab05/samples/phones.csv', r'data/lab05/out/phones_from_csv.json')
```
<img width="337" height="119" alt="img2_5" src="https://github.com/user-attachments/assets/3e9de389-d407-4a6a-bad4-adfac0a952ca" /> <img width="391" height="397" alt="img2_6" src="https://github.com/user-attachments/assets/02f5e58b-47d5-45cc-89de-6e55ba13fef2" />


## Задание B

### функция csv_to_xlsx

```python
def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)

    if csv_file.suffix.lower() != ".csv":
        raise ValueError('входной файл должен иметь расширение .csv')
    if xlsx_file.suffix.lower() != ".xlsx":
        raise ValueError('выходной файл должен иметь расширение .xlsx')

    if not csv_file.exists():
             raise FileNotFoundError('файл отсутствует')

    with csv_file.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        
        data = list(reader)
        if not data:
            raise ValueError("CSV-файл пуст или не содержит строк с данными")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in data:
        ws.append(row)

    for col in ws.columns:
        col_letter = col[0].column_letter

        max_col = 0
        for cell in col:
            if cell.value != 0:
                max_col = max(max_col, len(str(cell.value)))

        ws.column_dimensions[col_letter].width = max(max_col, 8)

    ensure_parent_dir(xlsx_file)
    wb.save(xlsx_file)
```

1. Проверяет существование CSV-файла
2. Проверяет расширение .csv и .xlsx
3. Читает строки в кодировке UTF-8
4. Создаёт книгу Excel с помощью openpyxl
5. Добавляет строки CSV на лист Sheet1
6. Рассчитывает ширину столбцов
7. Сохраняет результат по указанному пути

### Тест-кейс

```python
csv_to_xlsx(r"data/lab05/samples/people.csv", r"data/lab05/out/people.xlsx")
csv_to_xlsx(r"data/lab05/samples/cities.csv", r"data/lab05/out/cities.xlsx")
```
<img width="306" height="158" alt="img2_1" src="https://github.com/user-attachments/assets/3ea66829-c3a7-45e0-ad22-2b1f08932076" /> <img width="329" height="196" alt="img3_1" src="https://github.com/user-attachments/assets/805abaf8-a53f-4c93-9454-7e389e36557c" />

<img width="323" height="157" alt="img2_3" src="https://github.com/user-attachments/assets/42b3242c-36dc-41a7-bf71-fc8aa1ee0d90" /> <img width="349" height="188" alt="img3_2" src="https://github.com/user-attachments/assets/0dfb4a80-bf9c-4939-b61c-731b3f64dd0a" />

### Свой пример

```python
csv_to_xlsx(r"data/lab05/samples/phones.csv", r"data/lab05/out/phones.xlsx") 
```
<img width="337" height="119" alt="img2_5" src="https://github.com/user-attachments/assets/d1ecdabb-85fe-47d5-8240-a2f4a92a09d9" /> <img width="376" height="142" alt="img3_3" src="https://github.com/user-attachments/assets/645650c9-312f-41f1-808e-7e1b74cbdd7c" />

