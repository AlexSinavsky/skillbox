numb = int(input('Кол-во человек: '))
numbOut = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', numbOut, 'человек.')
numbList = list(range(1, numb + 1))
out = 0

for step in range(numb - 1):
    print('Текущий круг людей', numbList)
    start_count = out % len(numbList)
    out = (start_count + numbOut - 1) % len(numbList)
    print('Начало счёта с номера', numbList[start_count])
    print('Выбывает человек под номером', numbList[out])
    numbList.remove(numbList[out])
print('Остался человек под номером', numbList)