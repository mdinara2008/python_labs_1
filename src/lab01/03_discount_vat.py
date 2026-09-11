price = float(input('price='))
discount = float(input('discount='))
vat = float(input('vat='))

base = price*(1-discount/100)
vat_amount = base*(vat/100)
total = base+vat_amount

base1 = f'{base:.2f}'
vat_amount1 = f'{vat_amount:.2f}'
total1 = f'{total:.2f}'

print('База после скидки: ', base1, '₽')
print('НДС: ', vat_amount1, '₽')
print('Итого к оплате: ', total1, '₽')