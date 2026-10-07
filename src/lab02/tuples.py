def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec, tuple):
        raise TypeError('На вход нужно подать кортеж (tuple)')
    if len(rec)!=3:
        raise ValueError('Кортеж должен содержать 3 элемента: ФИО, группа, GPA')

    fio, group, gpa = rec
    parts = fio.strip().split()

    if len(parts) == 0:
        raise ValueError('Пустое ФИО')
    elif len(parts)<2:
        raise ValueError('ФИО должно содержать минимум фамилию и имя')

    surname = parts[0].capitalize()
    if len(parts)==2:
        initials = f'{parts[1][0].upper()}.'
        form_fio = f'{surname} {initials}'
    elif len(parts)==3:
        initials = f'{parts[1][0].upper()}.{parts[2][0].upper()}.'
        form_fio = f'{surname} {initials}'
    else:
        raise ValueError('Введите корректное ФИО')

    group = group.strip()
    if len(group)==0:
        raise ValueError('Пустая группа')

    if not isinstance(gpa, (int, float)):
        raise TypeError('Неверный тип GPA')
    if not (0.0<=gpa<=5.0):
        raise TypeError('GPA должен быть в диапазоне от 0.0 до 5.0')

    res = f'{form_fio}, гр. {group}, GPA {gpa:.2f}'
    return res

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
