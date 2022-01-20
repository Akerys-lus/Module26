def func_fibonacci(cnt, pos_num, first, second):
    cnt = cnt + 1
    if pos_num > 2:
        sum_num = first + second
        first = second
        second = sum_num
        if cnt == pos_num - 2:
            print(second)
        else:
            func_fibonacci(cnt, pos_num, first, second)
    else:
        print(cnt)
    return cnt, first, second


first_num = 1
second_num = 1
count = 0
position_num = int(input('Введите позицию числа в ряде Фибоначчи: '))
func_fibonacci(count, position_num, first_num, second_num)
