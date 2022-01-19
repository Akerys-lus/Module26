def func_fibonacci(pos_num, first_num=1, second_num=1):
    # TODO сделайте рекурсивной функцией, она буквально в три строки
    i_position = 0
    while i_position < pos_num - 2:
        sum_num = first_num + second_num
        first_num = second_num
        second_num = sum_num
        i_position = i_position + 1
    print('Число:', second_num)


position_num = int(input('Введите позицию числа в ряде Фибоначчи: '))
func_fibonacci(position_num)


