lst_exam = []
result = 0


def func_calc(x, y, i, res):
    lst_actions = ['/', '-', '+', '**', '*', '%', '//']
    if i in lst_actions and x.isdigit() and y.isdigit():
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
    else:
        answer_error = input('Обнаружена ошибка в строке: {} {} {} Хотите исправить? '.format(x, i, y))
        if answer_error == 'да':
            new_line = input('Введите исправленную строку: ').strip().split()
            res = float(func_calc(new_line[0], new_line[2], new_line[1], result))
            return res


with open('calc.txt', 'r', encoding='utf8') as calc:
    for i_len in calc:
        lst_exam.append(i_len.strip().split())

for i_exam in lst_exam:
    # try:
    answer = float(func_calc(i_exam[0], i_exam[2], i_exam[1], result))
    result = result + answer
    # except TypeError:
        # print('Что-то пошло не так')

print('Сумма верных ответов: ', result)
