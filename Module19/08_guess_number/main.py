import random
list_number_true = ()
max_number = int(input('Введите максимальное число: '))
numbers = ''
random_numb = 0
for i in range(max_number):
    random_numb_list = [random.randint(1, max_number) for _ in range(5)]
    random_numb = set(random_numb_list)
    print('Нужное число есть среди вот этих чисел: ', end='')
    for numb_i in random_numb:
        print(str(numb_i), end=' ')
    answer = input('\nОтвет Артёма: ')
    if answer == 'Да':
        list_number_true = set(random_numb)

    elif answer == 'Нет':
        list_number_true = set(list_number_true) - set(random_numb)
    else:
        for _ in sorted(list_number_true):
            numbers += str(_) + ' '
        print('Артём мог загадать следующие числа:', numbers)
        break

# TODO Покажу вариант решения:
max_number = int(input('Введите максимальное число: '))
all_nums = set(range(1, max_number + 1))
possible_nums = all_nums

while True:
    guess = input('Нужное число есть среди вот этих чисел: ')
    if guess == 'Помогите!':
        break
    guess = {int(i_num) for i_num in guess.split()}
    answer = input('Ответ Артёма: ').lower()
    if answer == 'да':
        possible_nums &= guess
    else:
        possible_nums -= guess

print('Артём мог загадать следующие числа:', sorted(possible_nums))

