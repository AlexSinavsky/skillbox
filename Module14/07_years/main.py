start = int(input('Введите первый год: '))
finish = int(input('Введите второй год: '))

print('Года от', start, 'до', finish, 'с тремя одинаковыми цифрами:')
for years in range(start, finish + 1):
    first = str(years % 10)
    second = str((years // 10) % 10)
    year = str(years)
    count = 0
    count2 = 0
    for numb in year:
        if numb == first:
            count += 1
            if count == 3:
                print(years)
        elif numb == second:
            count2 += 1
            if count2 == 3:
                print(years)




