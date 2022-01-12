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

# TODO Результат работы программы не соответствует требуемуму:
# Сколько записей вносится в протокол? 4
# Записи (результат и имя):
# 1 запись: 1 foka
# 2 запись: 3 koka
# 3 запись: 3 titi
# 4 запись: 3 foka
#
# Итоги соревнований:
# 1 место. titi (3)

# TODO А ожидается такой вывод (правильный):
# Итоги соревнований:
# 1 место. koka (3)
# 2 место. titi (3)
# 3 место. foka (3)
