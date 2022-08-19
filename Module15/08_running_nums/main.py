listNumb = [1, 2, 3, 4, 5]
shift = int(input('Введите сдвиг: '))
print('Начальный список', listNumb)
for _ in range(shift):
    listNumb.append(0)
listCount = len(listNumb) - 1
for i in range(listCount):
    listNumb[listCount - i] = listNumb[listCount - i - shift]
for i in range(shift):
    listNumb[shift - 1 - i] = listNumb[listCount - i]
    listNumb.pop(listCount - i)
print('Сдвинутый список', listNumb)
