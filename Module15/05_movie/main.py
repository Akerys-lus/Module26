films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

favourites_films = []
films_number = int(input('Кол-во фильмов, которые хотите добавить:  '))

for i in range(1, films_number + 1):
    print(i, 'фильм: ', end='')
    movie = input()
    while movie not in films:
        print('Нет такого фильма!')
        movie = input('Выберете другой фильм: ')
    else:
        favourites_films.append(movie)

print('\nСписок любимых фильмов: ')
print(favourites_films)
