def summ (numb):
    summNumb = 0
    while numb > 0:
        summNumb += numb % 10
        numb //= 10
    print('Сумма цифр:', summNumb)
    return summNumb
def quantity (numb):
    count = 0
    while numb > 0:
        numb //= 10
        count += 1
    print('Количество цифр в числе: ', count)
    return (count)

numb = int(input('Введите число: '))
print('Разность суммы и количества цифр:', summ(numb) - quantity(numb))