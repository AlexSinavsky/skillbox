numb = 5#int(input('Кол-во человек: '))
numbOut = 7#int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', numbOut, 'человек')
numbList = list(range(1, numb + 1))
nextRoundOut = numbOut - len(numbList) - 1
start = 1
while len(numbList) > 1:
    for i in range(start, len(numbList)):
        print('\nТекущий круг людей:', numbList)
        print('Начало счёта с номера', start)
        print('Выбывает человек под номером:', numbList[nextRoundOut])
        numbList.pop(nextRoundOut)
        nextRoundOut = numbOut - len(numbList)
        start = nextRoundOut
        if nextRoundOut > len(numbList):
            nextRoundOut = abs(numbOut - len(numbList))
            start = nextRoundOut

print(numbList)

