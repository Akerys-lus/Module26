# first_number = input('Введите число: ')
# second_number = input('Введите число: ')
num = float(input(''))


def vice_num(num):
    num = str(num)
    whole_part = int(num)
    vice_head = ''
    vice_end = ''
    num_end = float(num) - whole_part
    while int(num_end) / float(num) != 1:
        num_end *= 10
    num_end = str(num_end)
    for sym in num:
        if sym == '.':
            vice_head = vice_head + sym
        vice_head = sym + vice_head

    for sym in num_end:
        vice_end = sym + vice_end
    vice = vice_head + vice_end
    print(vice)
    return vice


# summ_num = float(vice_num(first_number)) + float(vice_num(second_number))
vice_num(num)
# print(summ_num)
