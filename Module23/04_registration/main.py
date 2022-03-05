lst_name = []
good_logs = open('registrations_good.log', 'w', encoding='utf-8')
bad_logs = open('registrations_bad.log', 'w', encoding='utf-8')
try:
    with open('registrations.txt', 'r', encoding='utf-8') as fh:
        for i_line in fh:
            lst_name.append(i_line.strip().split())
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


fh.close()
good_logs.close()
bad_logs.close()
