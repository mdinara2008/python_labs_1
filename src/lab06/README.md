# ЛР6 — CLI‑утилиты с argparse (cat/grep‑lite + конвертеры): Техническое задание
## Задание A - Подкоманды в одном CLI

```python
import argparse
from pathlib import Path
from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text

def main():
    """Функция считывает аргументы командной строки через модуль argparse. 
    Выполняет валидацию входных данных (проверяет выбор подкоманды 
    и физическое существование файла на диске). 
    В зависимости от команды выводит пронумерованный текст (cat) 
    или рассчитывает Топ-N частоты слов в файле (stats).
    """
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if not args.command:
        parser.error("Необходимо выбрать подкоманду cat или stats. Используйте --help для справки.")

    input_path = Path(args.input)
    if not input_path.exists():
        parser.error(f"Файл не найден по указанному пути: '{args.input}'")

    try:
        if args.command == "cat":
            text = read_text(args.input).split('\n')
            if args.n:
                for i, line in enumerate(text, start=1):
                    print(f'{i}: {line}')
            else:
                for line in text:
                    print(line)
    
        elif args.command == "stats":
            text = read_text(args.input)
            normal = normalize(text)
            token = tokenize(normal)
            words_cnt = count_freq(token)
            top = top_n(words_cnt, args.top)

            print(f'Топ-{args.top} самых частых слов:')
            for words, count in top:
                print(f'{words}: {count}')
    
    except Exception as e:
        parser.error(f"Произошла ошибка при обработке файла: {e}")

if __name__ == "__main__":
    main()
```
### Запуск
```python
python3 -m src.lab06.cli_text cat --input data/samples/lab05/people.csv -n
python3 -m src.lab06.cli_text stats --input data/samples/lab05/people.txt --top 5
```

### Проверка

### cat
`people.csv`

<img width="985" height="124" alt="Image" src="https://github.com/user-attachments/assets/7c316a26-2796-4b1e-b9cd-e4dfad59a074" />

### stats
`people.txt`

<img width="850" height="92" alt="Image" src="https://github.com/user-attachments/assets/f2b27e0e-7aff-4815-b6c3-9f6d9560939c" />

<img width="1044" height="121" alt="Image" src="https://github.com/user-attachments/assets/245400bd-33e3-4646-91b0-ffd35645bf0d" />

## Задание B - CLI‑конвертер

```python
import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx
from pathlib import Path

def main():
    """Функция инициализирует парсер командной строки на базе argparse и настраивает 
    три независимых режима конвертации: json2csv, csv2json и csv2xlsx.
    Проверяет выбор подкоманды и выполняет валидацию наличия входного файла на диске.
    Перехватывает ошибки некорректных данных и системные сбои, выводя их 
    пользователю через метод parser.error.
    """
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", help="Преобразовать JSON в CSV")
    p1.add_argument("--in", dest="input", required=True, help="входной файл .json")
    p1.add_argument("--out", dest="output", required=True, help="выходной файл .csv")

    p2 = sub.add_parser("csv2json", help="Преобразовать CSV в JSON")
    p2.add_argument("--in", dest="input", required=True, help="входной файл .csv")
    p2.add_argument("--out", dest="output", required=True, help="выходной файл .json")

    p3 = sub.add_parser("csv2xlsx", help="Преобразовать CSV в Excel")
    p3.add_argument("--in", dest="input", required=True, help="входной файл .csv")
    p3.add_argument("--out", dest="output", required=True, help="выходной файл .xlsx")

    args = parser.parse_args()

    if not args.cmd:
        parser.error("Необходимо выбрать режим конвертации. Используйте --help.")

    in_path = Path(args.input)
    if not in_path.exists():
        parser.error(f"Исходный файл не найден: '{args.input}'")

    try:
        if args.cmd == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.cmd == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.cmd == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)

    except ValueError as e:
        parser.error(f"Ошибка валидации структуры данных: {e}")
    except Exception as e:
        parser.error(f"Oшибка при конвертации: {e}")

if __name__ == "__main__":
    main()  
```
### Запуск
```python
python3 -m src.lab06.cli_convert json2csv --in data/samples/lab05/people.json --out data/out/lab05/people_from_json.csv
python3 -m src.lab06.cli_convert csv2json --in data/samples/lab05/people.csv --out data/out/lab05/people_from_csv.json
python3 -m src.lab06.cli_convert csv2xlsx --in data/samples/lab05/people.csv --out data/out/lab05/people.xlsx
```

### Проверка

`json2csv`

<img width="354" height="616" alt="Image" src="https://github.com/user-attachments/assets/e6d15340-aac1-4e7d-8d11-964b72a13f2a" />

<img width="360" height="164" alt="Image" src="https://github.com/user-attachments/assets/1801aa46-23ec-432a-80f6-b0399d59e835" />

`csv2json`

<img width="316" height="167" alt="Image" src="https://github.com/user-attachments/assets/f51f764b-5e42-4458-bc66-1321b324a8ae" />

<img width="389" height="621" alt="Image" src="https://github.com/user-attachments/assets/77d0c987-df1d-4b53-aa90-301994b528d6" />

`csv2xlsx`

<img width="316" height="167" alt="Image" src="https://github.com/user-attachments/assets/f51f764b-5e42-4458-bc66-1321b324a8ae" />

<img width="271" height="136" alt="Image" src="https://github.com/user-attachments/assets/decda3f4-ad89-45bc-ac51-459953b04fc5" />

### Справка --help

`cli_text, cat, stats`

<img width="663" height="210" alt="Image" src="https://github.com/user-attachments/assets/074837f5-9932-4f19-837e-8e1673f18e90" />

<img width="698" height="121" alt="Image" src="https://github.com/user-attachments/assets/6287e1dc-5531-43e3-8c93-260b3239a4d9" />

<img width="985" height="124" alt="Image" src="https://github.com/user-attachments/assets/8b6ef055-4a96-4020-adc8-84632d5aff06" />

`cli_convert, json2csv, csv2json, csv2xlsx`

<img width="691" height="228" alt="Image" src="https://github.com/user-attachments/assets/e88852e3-d621-4ff7-8a4a-99d44c6c17d0" />

<img width="766" height="123" alt="Image" src="https://github.com/user-attachments/assets/e82491a7-35fe-4aa4-90de-8fefa0295c70" />

<img width="768" height="126" alt="Image" src="https://github.com/user-attachments/assets/8916bc85-820c-4963-874a-ff21f84b4907" />

<img width="765" height="126" alt="Image" src="https://github.com/user-attachments/assets/56f70d5d-0520-40d0-b420-aa1d3f7131f4" />








