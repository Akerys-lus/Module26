list_number_true = ()
max_number = int(input('Введите максимальное число: '))
numbers = ''
for i in range(max_number):
    number = input('Нужное число есть среди вот этих чисел: ').split()
    if number == ['Помогите!']:
        for _ in sorted(list_number_true):
            numbers += _ + ' '
        print('Артём мог загадать следующие числа:', numbers)
        break
    else:
        answer = input('Ответ Артёма: ')
    if answer == 'Да':
        list_number_true = set(number)
        print(list_number_true)
    elif answer == 'Нет':
        list_number_true = set(list_number_true) - set(number)
    print(set(list_number_true))
