count_rec = int(input('Сколько записей вносится в протокол? '))
list_players = {}

count = 0
print('Записи (результат и имя): ')

for i_rec in range(1, count_rec + 1):
    score, name = input('{} запись: '.format(i_rec)).split()
    if name in list_players:
        if score > list_players[name]:
            list_players[name] = score
    else:
        list_players[name] = score


sorted_values = sorted(list_players.values())
sorted_dict = {}


for i in sorted_values[::-1]:
    for k in list_players.keys():
        if list_players[k] == i:
            sorted_dict[k] = i


print('\nИтоги соревнований:')


for i_score, i_name in sorted_dict.items():
    if count >= 3:
        break
    count += 1
    print('{} место. {} ({})'.format(count, i_name, i_score))
