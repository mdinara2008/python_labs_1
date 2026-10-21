# ЛР4 — Файлы: TXT/CSV и отчёты по текстовой статистике
## Задание A

### read_text
```python
from pathlib import Path
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''
    Открывает файл на чтение и возвращает содержимое как одну строку.
    Кодировка по умолчанию UTF-8, чтобы выбрать другую, нужно передать её в параметр функции (например, encoding = "cp1251").
    Если файл не найден - FileNotFoundError.
    Если кодировка не подходит - UnicodeDecodeError.
    '''
    p = Path(path)
    return p.read_text(encoding=encoding)
```

### write_csv

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

img

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
#### Тест-кейс для непустого файла input.txt

img

#### Тест-кейс для пустого файла input.txt

img

#### Тест-кейс для файла input.txt с текстом 'Привет' в кодировке cp1251

img

