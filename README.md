# ЛР1 - Ввод/вывод и форматирование
## Задание 1
### Вывод информации с помощью f-строки (разные типы данных).

```python
name = input('Имя: ')
age = int(input('Возраст: '))
print(f'Привет, {name}!', f'Через год тебе будет {age+1}.')

![](./images/lab01/img_01.png)

## Задание 2
### Обработка чисел, вывод суммы и среднего.

```python
a,b = float(input('a: ').replace(',','.')), float(input('b: ').replace(',','.'))
sum1 = a+b
avg = (a+b)/2
print(f'sum={sum1:.2f}; avg={avg:.2f}')

![](./images/lab01/img_02.png)

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

![](./images/lab01/img_03.png)

## Задание 4
### Перевод минут в формат часы:минуты.

```python
m = int(input('Минуты: '))
hours = m//60 
min = m%60
print(f'{hours}:{min:02d}')

![](./images/lab01/img_04.png)

## Задание 5
### Поиск и вывод инициалов ФИО, подсчёт длины символов.

```python
fio = input('ФИО: ').split()
initials = f'{fio[0][0]}{fio[1][0]}{fio[2][0]}'.upper()
words = ' '.join(fio)
length = len(words)
print(f'Инициалы: {initials}.')
print(f'Длина (символов): {length}')

![](./images/lab01/img_05.png)

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

![](./images/lab01/img_06.png)











