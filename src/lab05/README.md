# ЛР5 — JSON и конвертации (JSON↔CSV, CSV→XLSX): Техническое задание
## Задание A

### функция json_to_csv
```python
def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок как в первом объекте.
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
<img width="347" height="612" alt="img1_1" src="https://github.com/user-attachments/assets/7f4362d6-381c-44d7-b720-da162ab26143" />
<img width="351" height="168" alt="img1_2" src="https://github.com/user-attachments/assets/77d6c833-fed8-499b-a272-79bcd79e2e65" />

### Свой пример

```python
json_to_csv(r'data/lab05/samples/phones.json', r'data/lab05/out/phones_from_json.csv')
```
<img width="347" height="395" alt="img1_3" src="https://github.com/user-attachments/assets/b0f94ad3-9d09-446f-845b-8a134553e58d" />
<img width="358" height="119" alt="img1_4" src="https://github.com/user-attachments/assets/6fc28968-9e24-4fb2-83d1-4fd36171fc77" />

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
<img width="306" height="158" alt="img2_1" src="https://github.com/user-attachments/assets/c127d22c-8c70-44cb-9cd1-2b3f89f8a895" /> <img width="384" height="615" alt="img2_2" src="https://github.com/user-attachments/assets/ae04abba-3638-4c81-b63f-715abd61c3b6" />

<img width="323" height="157" alt="img2_3" src="https://github.com/user-attachments/assets/b8e4489a-4b33-438e-825c-99d9f57c37b0" /> <img width="331" height="613" alt="img2_4" src="https://github.com/user-attachments/assets/d4f4469e-c156-408a-a7f2-08d5bcc97e24" />

### Свой пример

```python
csv_to_json(r'data/lab05/samples/phones.csv', r'data/lab05/out/phones_from_csv.json')
```
<img width="337" height="119" alt="img2_5" src="https://github.com/user-attachments/assets/560de4b6-30cd-4ecc-a60c-a6a552326598" /> <img width="391" height="397" alt="img2_6" src="https://github.com/user-attachments/assets/d880808e-ce04-4e21-ba3f-383c24efdab0" />

### Запуск из корня репозитория
`python3 -m src.lab05.json_csv`

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
            if cell.value is not None:
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
<img width="306" height="158" alt="img2_1" src="https://github.com/user-attachments/assets/57bd7063-5b03-467a-8942-d7e976d7095f" /> <img width="329" height="196" alt="img3_1" src="https://github.com/user-attachments/assets/76e78a0e-9c5b-41be-a2e5-ca70f4ea7417" />

<img width="323" height="157" alt="img2_3" src="https://github.com/user-attachments/assets/89f794df-ee2d-4207-8280-aca28140772d" /> <img width="349" height="188" alt="img3_2" src="https://github.com/user-attachments/assets/a22609bd-aa45-4991-b6fe-a2840ce52f97" />

### Свой пример

```python
csv_to_xlsx(r"data/lab05/samples/phones.csv", r"data/lab05/out/phones.xlsx") 
```
<img width="337" height="119" alt="img2_5" src="https://github.com/user-attachments/assets/72175336-9275-47d9-b746-772884598810" /> <img width="376" height="142" alt="img3_3" src="https://github.com/user-attachments/assets/ac76532f-5f4d-4f87-af81-1787e8d8af83" />

### Запуск из корня репозитория
`python3 -m src.lab05.csv_xlsx`
