all_orders = {}

for i in range(1, int(input('Введите кол-во заказов: ')) + 1):
    (surname, order, amount) = input('{} заказ: '.format(i)).split()

    if order in str(all_orders):
        all_orders[surname][order] += int(amount)

    else:
        all_orders.setdefault(surname, {}).update({order: int(amount)})

    print(all_orders)
for name in all_orders:
    print(name + ':')
    for pizza in all_orders[name]:
        print('    ', pizza + ':', all_orders[name][pizza])
