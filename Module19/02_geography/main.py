count_countries = int(input('Введите кол-во стран: '))
list_countries = {}
for _ in range(1, count_countries + 1):
    country = input('{} страна: '.format(_)).split()
    for town in country[1:]:
        list_countries[town] = country[0]

for _ in range(1, 4):
    city = input('\n{} город: '.format(_))
    countries = list_countries.get(city)
    if city in list_countries:
        print('Город {} расположен в стране {}.'.format(city, countries))
    else:
        print('По городу {} данных нет.'.format(city))
