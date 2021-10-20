word = input('Введите слово: ')
unique_symbol = []

for i in word:
    count = 0
    for symb in word:
        if i == symb:
            count += 1
    if count == 1:
        unique_symbol.append(i)

print('Кол-во уникальных букв: ', len(unique_symbol))