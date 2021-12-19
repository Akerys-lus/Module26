all_orders = {}
orders = []

for i in range(1, int(input('Введите кол-во заказов: ')) + 1):
    orders = []
    (surname, order, amount) = input('{} заказ: '.format(i)).split()
    orders.append(str(order + ': ' + amount))
    all_orders.setdefault(surname, []).append(orders)

for i in all_orders:
    print(i, ':')
    for _ in sorted(all_orders[i]):
        for _ in _:
            print('    ', str(_))


