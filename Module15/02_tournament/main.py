playersList = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
print('Общий список участиков соревнований:', playersList)
firstDayList = []
count = 0
for players in playersList:
    count += 1
    if count % 2 == 0:
        firstDayList.append(players)
print('Список участников первого дня соревнований', firstDayList)