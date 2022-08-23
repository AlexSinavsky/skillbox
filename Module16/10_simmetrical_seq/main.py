numb = int(input('Количество цифр: '))

numbBase = []
for _ in range(numb):
    numbers = int(input('Число: '))
    numbBase.append(numbers)
print('Последовательность', numbBase)

count = 0
for i_numb in range(len(numbBase)-1, 0, -1):
    print(numbBase[i_numb], numbBase[i_numb - 1])
    if numbBase[i_numb] == numbBase[i_numb - 1]:
        count += 1
#    print(i_numb, end='')
print('Нужно приписать чисел:', count)