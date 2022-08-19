numb = int(input('Введите количество контейнеров: '))
base = []
count = 0
while len(base) < numb:
    weight = int(input('Введите массу контейнера: '))
    if weight <= 0 or weight > 200:
        print('Вес контейнера не может быть равен или меньше 0, и не должен превышать 200 кг')
    elif count != 0 and weight > base[count-1]:
        print('Вес следующего контейнера не должен превышать вес предыдущего')
    else:
        base.append(weight)
        count += 1

newCont = int(input('Введите вес нового контейнера: '))
base.append(newCont)
count = 0
for weight in base:
    if weight < newCont:
        print('Номер, куда встанет новый контейнер:', count+1)
        break
    count += 1
