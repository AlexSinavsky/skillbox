numb = int(input('Введите число: '))
for divisor in range(2, numb + 1):
    if numb % divisor == 0:
       print('Наименьший делитель, отличный от единицы:', divisor)
       break
