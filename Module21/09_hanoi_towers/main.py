def tower(n, x, y):
    if n == 1:
        print('Перенести диск 1 со стержня {} на стержень {}'.format(x, y))
    else:
        tower(n - 1, x, 6 - x - y)
        print('Перенести диск {} со стержня {} на стержень {}'.format(n, x, y))
        tower(n - 1, 6 - x - y, y)


count_disk = int(input('Введите кол-во дисков: '))
tower(count_disk, 1, 3)
