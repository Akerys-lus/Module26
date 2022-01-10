count = True
phonebooks = {}
while count:
    question = int(input('Введите номер действия: \n1. Добавить контакт \n2. Найти человека\n'))
    if question == 1:
        (name, surname) = input('Введите имя и фамилию нового контакта (через пробел): ').split()

        if (name, surname) in phonebooks:
            print('Такой человек уже есть в контактах.')
        else:
            phone_numb = int(input('Введите номер телефона: '))
            phonebooks.update({(name, surname): phone_numb})

        print('Текущий словарь контактов: ', phonebooks)

    elif question == 2:
        full_name = ''
        search_surname = input('Введите фамилию для поиска: ')
        for name, number in phonebooks.items():
            if str(search_surname).lower() in str(name).lower():
                print(name[0], name[1], number)
            else:
                print('Человек не найден.')
    else:
        print('Команда не корректна, попробуйте ещё раз.')
