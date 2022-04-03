class MyDict(dict):
    """
    Базовый класс Мой словарь

    """
    def get(self, key, default=0):
        """

        :param key: ключ
        :type: str
        :param default: значение
        :type: int
        :return: ключ со значением 0
        """
        return dict.get(self, key, default)


a = dict(a=1, b=2)
b = MyDict(a=1, b=2)
