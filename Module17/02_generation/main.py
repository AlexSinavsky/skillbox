number = int(input('Введите длину списка: '))
numbList = []
for i_numb in range(number):
  if i_numb % 2 == 0:
    numbList.append(1)
  else:
    if i_numb < 5:
      numbList.append(i_numb)
    else:
      numbList.append(i_numb - 5)
print('Результат', numbList)