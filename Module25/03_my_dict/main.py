class MyDict(dict):
    """
    Базовый класс Мой словарь

    """
    def get(self, key):
        """

        :param key: ключ
        :type: str
        :return: ключ со значением 0
        """
        return super().get(key, 0)


a = dict(a=1, b=2)
b = MyDict(a=1, b=2)

