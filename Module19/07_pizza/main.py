all_orders = {}

for i in range(1, int(input('Введите кол-во заказов: ')) + 1):
    (surname, order, amount) = input('{} заказ: '.format(i)).split()

    if order not in str(all_orders):

        all_orders.setdefault(surname, {}).update({order: int(amount)})
    else:
        all_orders[surname][order] += int(amount)


for name in all_orders:
    print(name + ':')
    for pizza in all_orders[name]:
        print('    ', pizza + ':', all_orders[name][pizza])
