word = input('Введите слово: ')
count = 0
countUnic = 0
for letters in word:
    for i in word:
        if letters == i:
            countUnic += 1
    if countUnic == 1:
        count += 1
    countUnic = 0
print('Количество уникальных букв', count)