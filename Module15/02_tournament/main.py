list_name = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
list_name_second = []
print(list_name, 'список всех участников')
count = 1
for name in list_name:
    count += 1
    if count % 2 != 0:
        list_name_second.append(name)
print('\nСписок участников, которые прошли в полуфинал: ', list_name_second)
