text = input('Введите строку: ')
count = 0

for i in text:
    if text.count(i) % 2 != 0:
        count += 1
if count >= 2:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')
