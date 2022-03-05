user = input('Введите имя: ')

while True:
    print('Чтобы посмотреть текущий текст чата - введите <0>')
    print('Чтобы отправить сообщение - введите <1>')
    action = input()

    if action == '0':

        try:
            with open('chat.txt', 'r', encoding='utf-8') as file:
                for i_message in file:
                    print(i_message, end='')
        except FileNotFoundError:
            print('История сообщений пуста. \n')

    elif action == '1':
        message = input('Введите сообщение: ')
        with open('chat.txt', 'a', encoding='utf-8') as file:
            file.write(f' { user } : { message } \n')
    else:
        print('Такой команды нет')
