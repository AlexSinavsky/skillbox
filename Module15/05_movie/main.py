films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favouriteFilms = []
findFilm = input('Введите название нужного фильма: ')
turn = 0
while findFilm != 'нет' or findFilm != 'Нет':
    for movie in films:
        if movie == findFilm:
            print('Рецензия найдена. Фильм добавлен в список любимых')
            print()
            favouriteFilms.append(movie)
            turn += 1
    if turn == 0:
        print('Рецензии на этот фильм еще нет')
        print()
    turn = 0
    print('Будете еще искать? Да - Введите название фильма / Нет - Введите "нет":', end='')
    findFilm = input()
    if findFilm == 'нет' or findFilm == 'Нет':
        print('Список любимых фильмов', favouriteFilms)
        break
