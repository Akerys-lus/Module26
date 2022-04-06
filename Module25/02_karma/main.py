import random


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


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


def check(num):
    if num != 1:
        num_exc = random.randint(1, 5)
        if num_exc == 1:
            raise KillError('Совершил убийство.')
        if num_exc == 2:
            raise DrunkError('Выпил слишком много.')
        if num_exc == 3:
            raise CarCrashError('Попал в аварию.')
        if num_exc == 4:
            raise GluttonyError('Переел.')
        if num_exc == 5:
            raise DepressionError('Впал в депрессию.')


def one_day(count):
    with open('karma.log', 'a', encoding='utf8') as karma_log:
        try:
            random_num = random.randint(1, 10)
            check(random_num)
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as exc:
            misconduct = f'{exc.__class__.__name__}'
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
