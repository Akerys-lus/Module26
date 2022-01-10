import random

list_numb = [random.randint(0, 10) for _ in range(10)]

print('Оригинальный список: ', list_numb)

new_list = [(list_numb[i], list_numb[i + 1]) for i in range(0, len(list_numb), 2)]

print(new_list)

new_list_two = list(zip(list_numb[0::2], list_numb[1::2]))

print(new_list_two)