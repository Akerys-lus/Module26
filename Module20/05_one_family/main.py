register = {
    'Сидоров Иван': 20,
    'Сидоров Евгений': 27,
    'Сидорова Дарья': 18,
    'Петров Сергей': 34,
    'Петров Иван': 21,
    'Абазина Елена': 35
}

surname = input('Введите фамилию: ')

for i_surname, age in register.items():
    if surname[1:len(surname) - 3] in i_surname:
        print(i_surname, age)
