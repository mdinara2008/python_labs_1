fio = input('ФИО: ').split()
initials = f'{fio[0][0]}{fio[1][0]}{fio[2][0]}'.upper()
words = ' '.join(fio)
length = len(words)
print(f'Инициалы: {initials}.')
print(f'Длина (символов): {length}')

