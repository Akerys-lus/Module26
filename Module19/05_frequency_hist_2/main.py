text = input('Введите текст: ')
dict_symb = {}
count = 0

print('Оригинальный словарь частот: ')

for symb in text:
    count_symb = text.count(symb)
    dict_symb.update({symb: count_symb})

for i in dict_symb:
    print(i, ':', dict_symb[i])

print('Инвертированный словарь частот:')
for _ in range(1, max(dict_symb.values()) + 1):
    ready_dict = []
    for i in dict_symb.keys():
        if dict_symb[i] == _:
            ready_dict.append(i)
    print(_, ':', ready_dict)





