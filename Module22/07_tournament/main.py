import os

first_tour_file = open('first_tour', 'r', encoding="utf8")
flag = True
needs_point = 0
list_players = []
dict_win = {}
for i_len in first_tour_file:
    if flag:
        needs_point = int(i_len)
        flag = False
    else:
        num = ''
        for i_symb in i_len:
            if i_symb.isnumeric():
                num += str(i_symb)
                int_num = int(num)
                if int_num > needs_point:
                    list_players.append(i_len.split(' '))

first_tour_file.close()

for i_players in list_players:
    point = ''
    for i_num in i_players[2]:
        if i_num.isnumeric():
            point += str(i_num)
    dict_win[i_players[1] + '.', i_players[0]] = point

sorted_values = sorted(dict_win.values())
sorted_dict = {}

for i in sorted_values[::-1]:
    for k in dict_win.keys():
        if dict_win[k] == i:
            sorted_dict[k] = i

count = 0
string = ''
for i_name, i_score in sorted_dict.items():
    full_name = ''
    for i in i_name:
        if full_name == '':
            full_name = full_name + i[0] + '. '
        else:
            full_name = full_name + i + ' '
    count += 1
    string += '{}) {}{}'.format(count, full_name, i_score) + '\n'

string = str(len(sorted_dict)) + '\n' + string
ready_file = open('second_tour.txt', 'w', encoding="utf8")
ready_file.write(string)
ready_file.close()
