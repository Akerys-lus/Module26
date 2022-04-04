class MyDict(dict):
    """
    Базовый класс Мой словарь

    """
    def get(self, key, default=0):  # TODO убираем default совсем, по заданию нет возможности менять значение по-умолчанию
        """

        :param key: ключ
        :type: str
        :param default: значение
        :type: int
        :return: ключ со значением 0
        """
        return dict.get(self, key, default)  # TODO сделаем более популярным способом:
                                             #  return self.get(key, 0)


a = dict(a=1, b=2)
b = MyDict(a=1, b=2)
