number = int(input('Введите длину списка: '))
numbList = [(1 if numb % 2 == 0 else numb % 5) for numb in range(number)]
print('Результат', numbList)
