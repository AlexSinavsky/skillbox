numbFriend = int(input('Количество друзей: '))
numbNote = int(input('Количество расписок: '))

friendCount = []
for i_friend in range(numbFriend):
    friendCount.append(0)

for i_note in range(numbNote):
    print('Расписка', i_note + 1)
    forWhom = int(input('Кому: '))
    fromWho = int(input('От кого: '))
    howMany = int(input('Сколько: '))
    print()
    friendCount[forWhom-1] -= howMany
    friendCount[fromWho-1] += howMany

print('Баланс друзей:')
for i_friend in range(numbFriend):
    print(i_friend + 1, ':', friendCount[i_friend])