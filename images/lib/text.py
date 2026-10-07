#lab02

def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
# возвращает кортеж из наименьшего и наибольшего чисел 
# из входного списка

def unique_sorted(nums: list[float | int]) -> list[float | int]:
# возвращает отсортированный список уникальных чисел в порядке возрастания

def flatten(mat: list[list | tuple]) -> list:
#расплющивает список списков/кортежей в один список по строкам

def transpose(mat: list[list[float | int]]) -> list[list]:
#меняет строки и столбцы прямоуг. матрицы местами

def row_sums(mat: list[list[float | int]]) -> list[float]:
#сумма по каждой строке прямоуг. матрицы

def col_sums(mat: list[list[float | int]]) -> list[float]:
#сумма по каждому столбцу прямоуг. матрицы

def format_record(rec: tuple[str, str, float]) -> str:
#форматирует элементы кортежа в единую строку 