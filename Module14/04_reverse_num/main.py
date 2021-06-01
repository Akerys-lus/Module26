first_number = input('Введите число: ')
second_number = input('Введите число: ')

def vice_num(num):
    vice = ''
    for sym in num:
        if sym == '.':
            vice = vice + sym
        else:
            vice = sym + vice

summ_num = float(vice_num(first_number) + vice_num(second_number))