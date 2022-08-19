numb = int(input('Введите число N: '))
numbList=[]
for numbers in range(1, numb + 1):
    if numbers % 2 != 0:
        numbList.append(numbers)
print('Список не четных цифр от 1 до', numb, ':', numbList)

