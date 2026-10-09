# ЛР3 — Тексты и частоты слов (словарь/множество)
## Задание A
### normalize

```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    newtext = ' '.join(text.split())
    if casefold==True:
        newtext = newtext.casefold()
    else:
        newtext = newtext.lower()

    if yo2e==True:
        newtext = newtext.replace('ё','е').replace('Ё','Е')

    return newtext
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
```

img

### tokenize

```python
def tokenize(text: str) -> list[str]:
    newtext = normalize(text)

    from re import findall
    return findall(r'\w+(?:-\w+)*', newtext)
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
```

img

### count_freq

```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for t in tokens:
        freq[t] = freq.get(t,0) + 1
    return freq
print(count_freq(["a","b","a","c","b","a"]))
print(count_freq(["bb","aa","bb","aa","cc"]))
```

img

### top_n

```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    res = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    return res[:n]
print(top_n({"a":3,"b":2,"c":1},2))
print(top_n({"aa":2,"bb":2,"cc":1},2))
```

img

