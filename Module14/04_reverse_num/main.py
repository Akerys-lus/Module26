def vice_num(num):
    whole_part = int(num)
    num = str(num)
    vice_head = ''
    vice_end = ''
    num_end = float(num) - whole_part
    while int(num_end) / float(num_end) != 1.0:
        num_end *= 10
    num_end = str(int(num_end))
    for sym in str(whole_part):
        vice_head += sym
    vice_head += '.'

    for sym in num_end:
        vice_end += sym
    vice = vice_head + vice_end
    return vice


number_one = float(input('Введите первое число: '))
number_two = float(input('Введите первое число: '))
number_one = vice_num(number_one)
number_two = vice_num(number_two)
print('Первое число наоборот:', float(number_one))
print('Второе число наоборот:', float(number_two))

print('Сумма чисел:', float(number_one) + float(number_two))
