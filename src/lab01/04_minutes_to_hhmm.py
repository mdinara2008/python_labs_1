m = int(input('Минуты: '))
hours = m//60 #полные часы
min = m%60 #оставшиеся минуты
print(f'{hours}:{min:02d}')
