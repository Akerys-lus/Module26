count_elements = int(input('Кол-во элементов: '))
start_list = []
finish_list = []

for i in range(count_elements):
    element = input('Введите элемент списка: ')
    start_list.append(element)

shift = int(input('Сдвиг: '))
index = 0
while index < count_elements - 1:
    empty_place = start_list[index]
    start_list[index] = start_list[index - shift]
    start_list[index - shift] = empty_place
    index += 1
print(start_list)