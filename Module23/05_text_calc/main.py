lst_exam = []
result = 0


def func_calc(x, y, i):
    try:
        if i == '/':
            return int(x) / int(y)
        if i == '//':
            return int(x) // int(y)
        if i == '%':
            return int(x) % int(y)
        if i == '*':
            return int(x) * int(y)
        if i == '**':
            return int(x) ** int(y)
        if i == '+':
            return int(x) + int(y)
        if i == '-':
            return int(x) - int(y)
    except ValueError:
        print('Что-то пошло не так')


with open('calc.txt', 'r') as calc:
    for i_len in calc:
        lst_exam.append(i_len.strip().split())

for i_exam in lst_exam:
    try:
        answer = float(func_calc(i_exam[0], i_exam[2], i_exam[1]))
        result = result + answer
    except TypeError:
        print('Что-то пошло не так')

print('Сумма верных ответов: ', result)
