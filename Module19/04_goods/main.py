goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for item in goods:  # TODO скорее это name
    name = item  # TODO лишняя переменная
    number_name = goods[name]
    count = 0
    price = 0
    for i in range(0, len(store[number_name])):  # TODO итерируйте по списку store[goods[name]]: тогда код будет проще,
                                                 #  а вместь i назовите item
        count += store[number_name][i]['quantity']
        price += store[number_name][i]['quantity'] * store[number_name][i]['price']
    print(name, '-', count, 'шт. Стоимость', price, 'руб.')
