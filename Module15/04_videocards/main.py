product_list_nvidia = []
updated_list_nvidia = []
max_count_nvidia = []
count = 1
quantity = int(input('Введите кол-во видеокарт: '))

for i in range(quantity):

    card = int(input(str(count) + ' Видеокарта: '))
    count += 1
    product_list_nvidia.append(card)
max_count_nvidia = max(product_list_nvidia)
for i in product_list_nvidia:
    if i != max_count_nvidia:
        updated_list_nvidia.append(i)
print('Новый список видеокарт: ', updated_list_nvidia)