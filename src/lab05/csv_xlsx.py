from openpyxl import Workbook
import csv
from pathlib import Path
from src.lab04.io_txt_csv import ensure_parent_dir

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

if __name__ == "__main__":
    csv_to_xlsx(r"data/lab05/samples/people.csv", r"data/lab05/out/people.xlsx")
    csv_to_xlsx(r"data/lab05/samples/cities.csv", r"data/lab05/out/cities.xlsx")
                 
    csv_to_xlsx(r"data/lab05/samples/phones.csv", r"data/lab05/out/phones.xlsx")       
             
         

    