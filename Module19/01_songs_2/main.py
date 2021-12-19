violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
count_time = 0
count_songs = int(input('Сколько песен выбрать? '))
for i in range(count_songs):
    songs = input('Введите название песни: ')
    count_time += violator_songs[songs]

print('Общее время звучания песен: ', count_time, ' минут')
