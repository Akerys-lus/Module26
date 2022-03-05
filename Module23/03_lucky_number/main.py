import random

sum_numb = 0
lst_numb = open('out_file.txt', 'w')
errors = [ArithmeticError, AssertionError, AttributeError, ZeroDivisionError, BufferError, MemoryError]

try:
    while sum_numb < 777:
        numb = int(input('Введите число: '))
        probabli = random.randint(1, 13)

        if probabli == 1:
            raise errors[random.randint(0, len(errors) - 1)]('Вас постигла неудача!')
        sum_numb += numb
        lst_numb.write(str(numb) + '\n')
    print('Вы успешно выполнили условие для выхода из порочного цикла!')
finally:
    lst_numb.close()
