all_orders = {}
orders = []

for i in range(1, int(input('Введите кол-во заказов: ')) + 1):
    orders = []
    (surname, order, amount) = input('{} заказ: '.format(i)).split()
    orders.append(str(order + ': ' + amount))
    all_orders.setdefault(surname, []).append(orders)
    # TODO если одна и таже пицца заказана одним заказчиком несколько раз, то записи должны объединяться, а количество
    #  таких пицц суммироваться, а не записываться отдельными записями

for i in all_orders:
    print(i, ':')
    for _ in sorted(all_orders[i]):  # TODO Назовите переменную полным словом, ведь она используется в коде
        for _ in _:  # TODO Аналогично предыдущему
            print('    ', str(_))


