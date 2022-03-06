lst_name = []
good_logs = open('registrations_good.log', 'w', encoding='utf-8')
bad_logs = open('registrations_bad.log', 'w', encoding='utf-8')
try:
    with open('registrations.txt', 'r', encoding='utf-8') as fh:
        for i_line in fh:
            lst_name.append(i_line.strip().split())
            # TODO не нужно все данные помещать из файла в список, файл может быть очень большой. Надо сделать так:
            #  1) передаём i_line функции валидации, при выбрасываии исключения указывайте поясняющие сообщения в
            #  круглых скобках, тогда обработку исключений можно сделать одной веткой.
            #  2) если функция валидации выбросила исключение то записать в лог обрабатываемую строку и поясняющее
            #  сообщение к исключению
            #  3) так как обработка во всех исключений идентична, поэтому можно сделать обработку одной веткой except,
            #  для чего укажите кортеж классов вместо одного класса, а сообщение записывайте в лог так:
            #  except (NameError, ...) as exc:
            #      error_message = f'{i_line.rstrip()} - {exc.__class__.__name__} - {exc}\n'
            # TODO (ловить исключения и обрабатывать их надо тут, а не в функции валидации

except FileNotFoundError:
    print('Файл не найден.')

for i_elem in lst_name:
    str_elem = ''
    if 3 > len(i_elem):
        if not i_elem == '\n':
            for ind in i_elem:
                str_elem += str(ind)
            bad_logs.write(str_elem
                           + ' ' * 8 + 'НЕ присутствуют все три поля: IndexError\n')
    else:
        if not i_elem[0].isalpha():
            bad_logs.write(str(i_elem[0] + ' ' + i_elem[1] + ' ' + i_elem[2])
                           + ' ' * 8 + 'поле имени содержит НЕ только буквы: NameError\n')
        elif '@' and '.' not in i_elem[1]:
            bad_logs.write(str(i_elem[0] + ' ' + i_elem[1] + ' ' + i_elem[2])
                           + ' ' * 8 + 'поле емейл НЕ содержит @ и .(точку): SyntaxError\n')
        elif not 10 < int(i_elem[2]) < 99:
            bad_logs.write(str(i_elem[0] + ' ' + i_elem[1] + ' ' + i_elem[2])
                           + ' ' * 8 + 'поле возраст НЕ является числом от 10 до 99: ValueError\n')
        else:
            good_logs.write(str(i_elem[0] + ' ' + i_elem[1] + ' ' + i_elem[2]) + '\n')


fh.close()  # TODO файл закрыт автоматически контекстным менеджером
good_logs.close()
bad_logs.close()
