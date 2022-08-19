print('Кол-во клеток: 5')
effectList = [3, 0, 6, 2, 10]
wrongList = []
count = 0
for _ in effectList:
    print('Эффективность', count + 1, 'клетки =', effectList[count])
    if effectList[count] < count + 1:
        wrongList.append(effectList[count])
    count += 1
print('Неподходящие значения', wrongList)


