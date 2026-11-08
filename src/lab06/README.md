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

#### cat
`people.csv`

img

img

#### stats
`people.txt`

img

img


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

img

`csv2json`

img

`csv2xlsx`

img

### Справка --help

`cli_text, cat, stats`

img

img

`cli_convert, json2csv, csv2json, csv2xlsx`

img10

img7

img8

img9








