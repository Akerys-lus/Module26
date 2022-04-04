import random


class Buddhist:
    """"
    Базовый класс Буддист

    Args:
        karma (int): передает кол-во кармы человека
    """
    def __init__(self, karma=0):
        self.karma = karma

    def get_karma(self):
        """
        Геттер для получения величины кармы

        :return: karma
        :rtype: int
        """
        return self.karma

    def set_karma(self, enlightenment):
        """
        Сеттер для увеличения величины кармы

        :param: enlightenment: просветление
        :type: int
        """
        self.karma += enlightenment
        buddhist.get_karma()  # TODO 1) не хорошая практика использовать глобальные переменные в коде класса
                              #  2) эта строка buddhist.get_karma() тут ничего не делает, убирайте


def one_day(count):
    if random.randint(1, 10) == 1:
        with open('karma.log', 'a', encoding='utf8') as karma_log:
            misconduct = random.choice(['KillError', 'DrunkError',
                                        'CarCrashError', 'GluttonyError', 'DepressionError'])
            # TODO Согласно заданию: "выкинуть одно из исключений", а не выбрать строку из списка. Создайте кастомные
            #  исключения с указанными именами, наследуйте их от Exception, а в качестве реализации класса достаточно
            #  указать pass, так как всё остальное уже реализовано в базовом классе. В списке выше вместо строк имён
            #  классов используйте объекты исключений с поясняющими сообщениями. Ловить исключения и логгировать их надо
            #  в основном коде программы (вспомните задачу 4 из модуля 23)
            karma_log.write(f'День {count}: поступок {misconduct}\n')
            return False
    else:
        return random.randint(1, 7)


buddhist = Buddhist()
day = 0

while buddhist.get_karma() < 500:
    day += 1
    if one_day(day):
        pass
    else:
        buddhist.set_karma(one_day(day))

print('Вы достигли просветления.')
