skiNumb = int(input('Количество коньков: '))
skiBase = []
for i_ski in range(skiNumb):
    print('Размер', i_ski + 1, 'пары: ', end=' ')
    skiSize = int(input())
    skiBase.append(skiSize)

peopleNumb = int(input('Количество людей: '))
peopleBase = []
for i_pl in range(peopleNumb):
    print('Размер ноги', i_pl + 1, 'человека: ', end=' ')
    legSize = int(input())
    peopleBase.append(legSize)

match = 0
for i_ski in range(len(skiBase)):
    for i_pl in range(len(peopleBase)):
        if skiBase[i_ski] == peopleBase[i_pl]:
            match += 1
print('Наибольшее кол-во людей, которые могут взять ролики:', match)