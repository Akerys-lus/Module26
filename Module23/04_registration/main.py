class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def check(line):
    name, mail, age = line.split(' ')
    symbols = ('@', '.')
    age = int(age)
    if name.isalpha() is False:
        raise NotNameError('Ошибка в имени!')  # TODO вот так указываем поясняющее сообщение...
    elif age not in range(10, 100):
        raise ValueError()  # TODO ...добавьте аналогично сюда и четырьмя строками ниже
    else:
        for char in symbols:
            if char not in mail:
                raise NotEmailError
    return line


# TODO Открываем все три файла одним контекстным менеджером:
with open('registrations_.txt', mode='r', encoding='utf-8') as ff, \
    open('registration_bad.txt', mode='r', encoding='utf-8') as bad_log, \
        open('registration_good.txt', mode='r', encoding='utf-8') as good_log:
    for line in ff:
        line = line[:-1]
        try:
            string = check(line)
        except NotNameError:
            # TODO Так как обработка во всех исключений идентична, поэтому можно сделать обработку
            #  одной веткой - укажите тут кортеж классов, а сообщение записывайте в лог так:
            #  except (NotNameError, ...) as exc:
            #      error_message = f'{i_line.rstrip()} - {exc.__class__.__name__} - {exc}\n'
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

