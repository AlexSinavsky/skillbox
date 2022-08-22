firstList = []
secondList = []

for _ in range(3):
    numb = int(input('Введите число в первый список: '))
    firstList.append(numb)
for _ in range(7):
    numb = int(input('Введите число во второй список: '))
    secondList.append(numb)
print('Первый список', firstList)
print('Второй список', secondList)
firstList.extend(secondList)
firstList = set(firstList)
print('Новый первый список с уникальными элементами', firstList)
