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
