def seq_range(txt, tpl):
    pairs = ((txt[i], tpl[i]) for i in range(min(len(txt), len(tpl))))   # используйте параметры, а не глобальные переменные
    print(pairs)
    print(list(pairs))


text = 'abcd'
tuple_list = (10, 20, 30, 40)
print('Строка: {}\nКортеж чисел: {}'.format(text, tuple_list))
seq_range(text, tuple_list)
