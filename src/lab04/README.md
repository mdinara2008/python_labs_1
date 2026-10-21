# ЛР4 — Файлы: TXT/CSV и отчёты по текстовой статистике
## Задание A

### функция read_text
```python
from pathlib import Path
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''
    Открывает файл на чтение и возвращает содержимое как одну строку.
    Кодировка по умолчанию UTF-8, чтобы выбрать другую, нужно передать её в параметр функции (например, encoding = "cp1251").
    Файл не найден -> функция не перехватывает ошибку,а даёт ей "всплыть" наружу как FileNotFoundError.
    Неподходящая кодировка -> "всплывает" UnicodeDecodeError.
    '''
    p = Path(path)
    return p.read_text(encoding=encoding)
```

### функция write_csv

```python
import csv
from pathlib import Path
from typing import Iterable, Sequence
def ensure_parent_dir(path: str | Path) -> None:
    '''
    Создаёт родительские директории, если их нет.
    '''
    Path(path).parent.mkdir(parents=True, exist_ok=True)

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    '''
    Создаёт/перезаписывает CSV с разделителем ','.
    Если передан header, то он записывается первой строкой.
    Проверяется, что каждая строка в rows имеет одинаковую длину (иначе ValueError).
    '''
    p = Path(path)
    rows = list(rows)

    length = {len(i) for i in rows}
    if header is not None:
        length.add(len(header))
    if len(length) > 1:
        raise ValueError('строки имеют разную длину')

    ensure_parent_dir(path)

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
            
if __name__ == "__main__":
    txt = read_text("data/lab04/input.txt", encoding="utf-8")
    print(txt)
    write_csv([("word","count"),("test",3)], "data/lab04/check.csv")
```

<img width="509" height="39" alt="Снимок экрана 2026-10-21 в 11 09 34" src="https://github.com/user-attachments/assets/0e0e1c25-d443-4128-af78-ece6bb979309" />

<img width="225" height="70" alt="Снимок экрана 2026-10-21 в 11 13 44" src="https://github.com/user-attachments/assets/6782f98e-77ae-4f5e-aad7-5dc324fc9ead" />


## Задание B

```python
import sys
from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv

def main():
    try:
        r_text = read_text("data/lab04/input.txt", encoding="utf-8")
    except FileNotFoundError:
        print("файл не найден")
        sys.exit(1)

    normal = normalize(r_text)
    token = tokenize(normal)
    c_freq_new = count_freq(token)
    top = top_n(c_freq_new)
    rows = sorted(c_freq_new.items(), key=lambda k: (-k[1], k[0]))

    write_csv(rows, "data/lab04/report.csv", header= ("word","count"))

    print(f'Всего слов: {len(token)}')
    print(f'Уникальных слов: {len(c_freq_new)}')
    print('Топ-5:')
    for t in top:
        print(f'{t[0]}: {t[1]}')

if __name__ == "__main__":
    main()
```

1. С помощью функции read_text читаем входной файл input.txt, путь к которому 'захардкожен' (data/lab04/input.txt).
2. Нормализует текст файла, токенизирует и считает частоты слов.
3. Сохраняет data/lab04/report.csv c колонками: word,count, отсортированными: count ↓, слово ↑ (при равенстве).
4. В консоль печатает краткое резюме:
    Всего слов: <N>
    Уникальных слов: <K>
    Топ-5:

### Тест-кейс для непустого файла input.txt

<img width="632" height="108" alt="Снимок экрана 2026-10-21 в 11 22 07" src="https://github.com/user-attachments/assets/1e3369f0-0d9a-49a0-af82-316f1acc85e2" />

<img width="236" height="99" alt="Снимок экрана 2026-10-20 в 23 12 44" src="https://github.com/user-attachments/assets/5a0b368f-89e7-424d-8d74-7c81b123c7b1" />

### Тест-кейс для пустого файла input.txt

<img width="632" height="71" alt="Снимок экрана 2026-10-20 в 23 14 55" src="https://github.com/user-attachments/assets/30320611-f567-4de2-9827-c61af745dbfc" />

<img width="225" height="78" alt="Снимок экрана 2026-10-21 в 11 28 34" src="https://github.com/user-attachments/assets/b5ddfee1-099b-42e0-87d9-fd099ef166be" />

### Тест-кейс для файла input.txt с текстом 'Привет' в кодировке cp1251

<img width="628" height="88" alt="Снимок экрана 2026-10-20 в 23 17 57" src="https://github.com/user-attachments/assets/133d3b63-35b9-4db7-8593-b4866e6ff013" />

<img width="227" height="68" alt="Снимок экрана 2026-10-21 в 11 34 40" src="https://github.com/user-attachments/assets/f208e3e0-3cfc-4bce-b107-df7efb7f536c" />

### Краевые случаи

#### io_txt_csv.py

1. Пустой файл → возвращается пустая строка.
2. Если файл очень большой, он по ТЗ будет читаться целиком, но в реальных ситуациях стоит читать построчно.
3. write_csv с пустым rows и header=None → создаётся пустой файл (0 строк). Если header=("a","b") → файл содержит только заголовок.

#### text_report.py

1. Если входного файла не существует → print("файл не найден"), sys.exit(1).
2. Входной файл пустой → report.csv будет содержать только заголовок.
3. Другая кодировка → указать параметр encoding = "..." в параметрах функции или --encoding ... при запуске из терминала.
