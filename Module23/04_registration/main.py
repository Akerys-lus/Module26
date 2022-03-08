class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def check(line):
    name, mail, age = line.split(' ')
    symbols = ('@', '.')
    age = int(age)
    if name.isalpha() is False:
        raise NotNameError('Ошибка в имени!')
    elif age not in range(10, 100):
        raise ValueError('Неподходящий возраст!')
    else:
        for char in symbols:
            if char not in mail:
                raise NotEmailError('Неправильный емейл!')
    return line


with open('registrations.txt', mode='r', encoding='utf-8') as ff, \
        open('registration_bad.txt', mode='w', encoding='utf-8') as bad_log, \
        open('registration_good.txt', mode='w', encoding='utf-8') as good_log:
    for line in ff:
        line = line[:-1]
        try:
            string = check(line)
        except (NotNameError, NotEmailError, ValueError) as exc:
            error_message = f'{line.rstrip()} - {exc.__class__.__name__} - {exc}\n'
            bad_log.write(error_message)
        else:
            good = open('registraton_good.log', mode='a', encoding='utf-8')
            good_log.write(line + '\n')

good_log.close()
