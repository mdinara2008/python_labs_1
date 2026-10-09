import sys
from src.lib.text import normalize, tokenize, count_freq, top_n

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
