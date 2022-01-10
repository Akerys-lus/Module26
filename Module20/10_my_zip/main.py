text = 'abcd'
tpl = (10, 20, 30, 40)

pairs = ((text[i], tpl[i])
         for i in range(min(len(text), len(tpl))))

print('Строка: {}\nКортеж чисел: {}'.format(text, tpl))

print(pairs)

for i in pairs:
    print(i)