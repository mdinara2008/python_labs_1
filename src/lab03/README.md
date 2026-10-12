# ЛР3 — Тексты и частоты слов (словарь/множество)
## Задание A
### normalize

```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    '''
    заменяет все ё/Ё на е/Е;
    заменяет управляющие символы \t, \r, \n на пробел;
    «схлопывает» последовательности пробелов в один;
    если casefold=True, то строка приводится к casefold;
    если casefold=False, то используем lower()
    '''
    newtext = ' '.join(text.split())
    if casefold==True:
        newtext = newtext.casefold()
    else:
        newtext = newtext.lower()

    if yo2e==True:
        newtext = newtext.replace('ё','е').replace('Ё','Е')

    return newtext
```

img

### tokenize

```python
def tokenize(text: str) -> list[str]:
    '''
    разбивает строку на «слова» по небуквенно-цифровым разделителям,
    в том числе слова с дефисом внутри и числа;
    эмодзи и спецсимволы не являются «словами»
    '''
    newtext = normalize(text)

    from re import findall
    return findall(r'\w+(?:-\w+)*', newtext)
```

img

### count_freq

```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    '''
    считает частоту токенов в списке;
    возвращает словарь, где ключ - сам токен, а значение - частота токенов;
    если частоты равны, сортировка по алфавитному порядку
    '''
    freq = {}
    for t in tokens:
        freq[t] = freq.get(t,0) + 1
    return freq
```

img

### top_n

```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    '''
    возвращает список из топ-N по убыванию частоты;
    если частоты равны, сортировка по алфавиту слова
    '''
    res = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    return res[:n]
```

img

## Задание B

Скрипт text_stats.py

```python
from src.lib.text import normalize, tokenize, count_freq, top_n
import sys

text = sys.stdin.read()
if text.strip()=='':
    raise ValueError('пустая строка')

normal = normalize(text)
token = tokenize(normal)
c_freq_new = count_freq(token)
top = top_n(c_freq_new)

print(f'Всего слов: {len(token)}')
print(f'Уникальных слов: {len(c_freq_new)}')
print('Топ-5:')
for t in top:
    print(f'{t[0]}: {t[1]}')
```

Запуск: в терминале - python -m src.lab03.text_stats
Ввод на одной строке или построчно.
Вывод: Control+D (Mac)

### Тест-кейсы

img

img