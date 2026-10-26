import json, csv
from pathlib import Path
from src.lab04.io_txt_csv import ensure_parent_dir

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


if __name__ == "__main__":
    json_to_csv(r'data/lab05/samples/people.json', r'data/lab05/out/people_from_json.csv')
    csv_to_json(r'data/lab05/samples/people.csv', r'data/lab05/out/people_from_csv.json')
    csv_to_json(r'data/lab05/samples/cities.csv', r'data/lab05/out/cities.json')


    json_to_csv(r'data/lab05/samples/phones.json', r'data/lab05/out/phones_from_json.csv')
    csv_to_json(r'data/lab05/samples/phones.csv', r'data/lab05/out/phones_from_csv.json')
