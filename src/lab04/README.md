# ЛР4 — Файлы: TXT/CSV и отчёты по текстовой статистике
## Задание A

### read_text
```python
from pathlib import Path
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''
    Открывает файл на чтение и возвращает содержимое как одну строку.
    Кодировка по умолчанию UTF-8, чтобы выбрать другую, нужно передать её в параметр функции (например, encoding = "cp1251").
    Файл не найден -> функция не перехватывает ошибку,а даёт ей "всплыть" наружу как FileNotFoundError.
    Если неподходящая кодировка -> "всплывает" UnicodeDecodeError.
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

<img width="509" height="39" alt="Снимок экрана 2026-10-21 в 11 09 34" src="https://github.com/user-attachments/assets/5b9bf498-fab9-4059-bd25-6febd9977e8a" />

<img width="225" height="70" alt="Снимок экрана 2026-10-21 в 11 13 44" src="https://github.com/user-attachments/assets/da4fc635-578d-4dc9-b656-16de8ea00354" />


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
    except UnicodeDecodeError:
        print("неподходящая кодировка") 
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

<img width="236" height="99" alt="Снимок экрана 2026-10-20 в 23 12 44" src="https://github.com/user-attachments/assets/a8d8d253-09cd-47f5-8834-fbaf1e847941" />

#### Тест-кейс для непустого файла input.txt

<img width="632" height="108" alt="Снимок экрана 2026-10-21 в 11 22 07" src="https://github.com/user-attachments/assets/fe94524e-9941-4adf-a360-29cfcd4096a4" />  

<img width="225" height="70" alt="Снимок экрана 2026-10-21 в 11 13 44" src="https://github.com/user-attachments/assets/ce8cc240-c252-4308-8443-74a5f103ad98" />

#### Тест-кейс для пустого файла input.txt

<img width="632" height="71" alt="Снимок экрана 2026-10-20 в 23 14 55" src="https://github.com/user-attachments/assets/791df74c-aada-4f4b-8dc8-5a025e4932bd" />

<img width="225" height="78" alt="Снимок экрана 2026-10-21 в 11 28 34" src="https://github.com/user-attachments/assets/8ba4d2b0-a530-44e3-a054-8a856f656fd1" />

#### Тест-кейс для файла input.txt с текстом 'Привет' в кодировке cp1251

<img width="628" height="88" alt="Снимок экрана 2026-10-20 в 23 17 57" src="https://github.com/user-attachments/assets/5890fa10-77c1-4fe1-a8cb-acceb8224f18" />

<img width="227" height="68" alt="Снимок экрана 2026-10-21 в 11 34 40" src="https://github.com/user-attachments/assets/97a6f8bc-60fa-42a6-9355-19ccdddee498" />
