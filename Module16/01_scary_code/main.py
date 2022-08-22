mainList = [1, 5, 3]
firstList = [1, 5, 1, 5]
secondList = [1, 3, 1, 5, 3, 3]

mainList.extend(firstList)
print('Количество цифр 5 при первом объединении', mainList.count(5))
for i in range(mainList.count(5)):
    mainList.remove(5)
mainList.extend(secondList)
print('Количество цифр 3 при втором объединении', mainList.count(3))
print('Итоговый список', mainList)
