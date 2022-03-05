import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


file = open('coordinates.txt', 'r')
file_2 = open('result.txt', 'w')
for line in file:
    nums_list = line.split()
    try:
        res_frt = f(float(nums_list[0]), float(nums_list[1]))
        res_sec = f2(float(nums_list[0]), float(nums_list[1]))
        number = float(random.randint(0, 100))
        my_list = sorted([res_frt, res_sec, number])
        print(my_list)
        file_2.write(str(my_list) + '\n')
    except ZeroDivisionError:
        print('Одно из чисел = 0')
