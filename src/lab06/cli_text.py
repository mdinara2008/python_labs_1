import argparse
from pathlib import Path
from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text

def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if not args.command:
        parser.error("Необходимо выбрать подкоманду cat или stats. Используйте --help для справки.")

    input_path = Path(args.input)
    if not input_path.exists():
        parser.error(f"Файл не найден по указанному пути: '{args.input}'")

    try:
        if args.command == "cat":
            text = read_text(args.input).splitlines()
            if args.n:
                for i, line in enumerate(text, start=1):
                    print(f'{i}: {line}')
            else:
                for line in text:
                    print(line)
    
        elif args.command == "stats":
            text = read_text(args.input)
            normal = normalize(text)
            token = tokenize(normal)
            words_cnt = count_freq(token)
            top = top_n(words_cnt, args.top)

            print(f'Топ-{args.top} самых частых слов:')
            for words, count in top:
                print(f'{words}: {count}')
    
    except Exception as e:
        parser.error(f"Ошибка при обработке файла: {e}")

if __name__ == "__main__":
    main()