count_rec = int(input('Сколько записей вносится в протокол? '))
list_players = {}
reverse_list = {}
count = 0
print('Записи (результат и имя): ')

for i_rec in range(1, count_rec + 1):
    score, name = input('{} запись: '.format(i_rec)).split()
    if name in list_players:
        if score > list_players[name]:
            list_players[name] = score
    else:
        list_players[name] = score

for i_name, i_score in list_players.items():
    reverse_list[i_score] = i_name

winners = list(reverse_list.items())
winners.sort()

print('\nИтоги соревнований:')

for i_score, i_name in winners[::-1]:
    if count >= 3:
        break
    count += 1
    print('{} место. {} ({})'.format(count, i_name, i_score))