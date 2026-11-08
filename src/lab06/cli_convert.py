import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx
from pathlib import Path

def main():
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