def seq_range(txt, tpl):
    pairs = ((text[i], tuple_list[i]) for i in range(min(len(text), len(tuple_list))))
    print(pairs)
    print(list(pairs))


text = 'abcd'
tuple_list = (10, 20, 30, 40)
print('Строка: {}\nКортеж чисел: {}'.format(text, tuple_list))
seq_range(text, tuple_list)
