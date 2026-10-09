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


def tokenize(text: str) -> list[str]:
    '''
    разбивает строку на «слова» по небуквенно-цифровым разделителям,
    в том числе слова с дефисом внутри и числа;
    эмодзи не являются «словами»
    '''
    newtext = normalize(text)

    from re import findall
    return findall(r'\w+(?:-\w+)*', newtext)


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


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    '''
    возвращает список из топ-N по убыванию частоты;
    если частоты равны, сортировка по алфавиту слова
    '''
    res = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    return res[:n]
print(top_n({"a":3,"b":2,"c":1},2))
print(top_n({"aa":2,"bb":2,"cc":1},2))