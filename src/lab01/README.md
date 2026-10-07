# ЛР1 - Ввод/вывод и форматирование
## Задание 1
### Вывод информации с помощью f-строки (разные типы данных).

```python
name = input('Имя: ')
age = int(input('Возраст: '))
print(f'Привет, {name}!', f'Через год тебе будет {age+1}.')
```
<img width="437" height="60" alt="img_01" src="https://github.com/user-attachments/assets/9589fd25-8141-4bd7-83b0-50ef72e77391" />


## Задание 2
### Обработка чисел, вывод суммы и среднего.

```python
a,b = float(input('a: ').replace(',','.')), float(input('b: ').replace(',','.'))
sum1 = a+b
avg = (a+b)/2
print(f'sum={sum1:.2f}; avg={avg:.2f}')
```

<img width="431" height="59" alt="img_02" src="https://github.com/user-attachments/assets/aaf85181-0a8b-4e5f-a15a-de04dfbd46af" />


## Задание 3
### Подсчёт базы после скидки, НДС и итоговой суммы.

```python
price = float(input('Цена, ₽: ').replace(',','.'))
discount = float(input('Скидка, %: ').replace(',','.'))
vat = float(input('НДС, %: ').replace(',','.'))

base = price*(1-discount/100)
vat_amount = base*(vat/100)
total = base+vat_amount

print(f'База после скидки: {base:.2f} ₽')
print(f'НДС:               {vat_amount:.2f} ₽')
print(f'Итого к оплате:    {total:.2f} ₽')
```

<img width="457" height="101" alt="img_03" src="https://github.com/user-attachments/assets/98b22c7e-9d3a-4a04-9b9d-eb16d948f935" />


## Задание 4
### Перевод минут в формат часы:минуты.

```python
m = int(input('Минуты: '))
hours = m//60 
min = m%60
print(f'{hours}:{min:02d}')
```

<img width="455" height="59" alt="img_04" src="https://github.com/user-attachments/assets/30453435-3bc6-4e62-a7b4-97345122d01a" />


## Задание 5
### Поиск и вывод инициалов ФИО, подсчёт длины символов.

```python
fio = input('ФИО: ').split()
initials = f'{fio[0][0]}{fio[1][0]}{fio[2][0]}'.upper()
words = ' '.join(fio)
length = len(words)
print(f'Инициалы: {initials}.')
print(f'Длина (символов): {length}')
```
<img width="452" height="72" alt="img_05" src="https://github.com/user-attachments/assets/bdcdb87e-745b-414c-972c-d94d0262452f" />


## Задание 6
### Обработка заданного n числа студентов, проверка на True/False в данных, подсчёт каждого типа.

```python
n = int(input('in_1: '))
ochno = 0
zaochno = 0
for i in range(n):
    l_name, name, age, format = input(f'in_{i+2}: ').split()
    if format=='True':
        ochno+=1
    else:
        zaochno+=1
print(f'out: {ochno} {zaochno}')
```
<img width="371" height="86" alt="img_06" src="https://github.com/user-attachments/assets/d225bdaf-fcfb-4a25-908d-e34b7a96edd6" />












