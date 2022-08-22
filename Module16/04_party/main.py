guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

question = ''
while question != 'пора спать':
    print('\nСейчас на вечеринке', len(guests), 'человек')
    print(guests)
    question = input('\nГость пришел или ушел? ')
    if question == 'пришел' or question == 'ушел' or question == 'пора спать':
        if question != 'пора спать':
            name = input('Имя гостя: ')
            if len(guests) < 6:
                if question == 'пришел':
                    print('Привет', name)
                    guests.append(name)
            else:
                print('Прости', name, 'но мест нет')
            if question == 'ушел':
                print('Пока,', name)
                guests.remove(name)
        else:
            print('Вечеринка закончилась, все легли спать.')
    else:
        print('Плохо слышно, повторите')
