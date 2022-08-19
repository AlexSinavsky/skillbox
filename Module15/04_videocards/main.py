print('Кол-во видеокарт: 5')
oldList = [3070, 2060, 3090, 3070, 3090]
newList = []
count = 0
newCardNumb = oldList[0]
for _ in oldList:
    print(count + 1, 'Видеокарта', oldList[count])
    if newCardNumb < oldList[count]:
        newCardNumb = oldList[count]
    count += 1
for cart in oldList:
    if cart < newCardNumb:
        newList.append(cart)
print('Старый список видеокарт:', oldList)
print('Новый список видеокарт:', newList)

