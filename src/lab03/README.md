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

<img width="469" height="264" alt="img03_1" src="https://github.com/user-attachments/assets/2e4716de-b0fa-4c26-a2d1-14b3a4431092" />


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

<img width="452" height="320" alt="img03_2" src="https://github.com/user-attachments/assets/e44aef33-bbda-43dc-a22a-a46fa38b7879" />


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

<img width="461" height="203" alt="img03_3" src="https://github.com/user-attachments/assets/293208c1-d5bb-4025-b827-b9c909decbbf" />


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

<img width="450" height="197" alt="img03_4" src="https://github.com/user-attachments/assets/6fb96eb1-db5d-4b79-8b9e-624622c49576" />


## Задание B

Скрипт читает текст из stdin, нормализует и токенизирует его с помощью функций из text.py, считает общее количество слов, количество уникальных слов и выводит топ-5 самых частых слов.

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
#### Запуск (в терминале)
```python
python3 -m src.lab03.text_stats
```

<img width="625" height="126" alt="img03_5" src="https://github.com/user-attachments/assets/7ba4e1fd-127b-41b3-bc38-ff99d3228c29" />
