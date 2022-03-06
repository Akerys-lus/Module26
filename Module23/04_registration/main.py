class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def check(line):
    name, mail, age = line.split(' ')
    symbols = ('@', '.')
    age = int(age)
    if name.isalpha() is False:
        raise NotNameError
    elif age not in range(10, 100):
        raise ValueError()
    else:
        for char in symbols:
            if char not in mail:
                raise NotEmailError
    return line


with open('registrations_.txt', mode='r', encoding='utf-8') as ff:
    for line in ff:
        line = line[:-1]
        try:
            string = check(line)
        except NotNameError:
            bad = open('registration_bad.log', mode='a', encoding='utf-8')
            bad.write(line + 'Имя содержит цифры' + '\n')
            bad.close()
        except NotEmailError:
            bad = open('registration_bad.log', mode='a', encoding='utf-8')
            bad.write(line + 'Некорректно указан E-mail' + '\n')
            bad.close()
        except ValueError:
            bad = open('registration_bad.log', mode='a', encoding='utf-8')
            bad.write(line + 'Неверные данные' + '\n')
            bad.close()
        else:
            good = open('registraton_good.log', mode='a', encoding='utf-8')
            good.write(line + '\n')
            good.close()
