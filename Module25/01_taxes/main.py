class Property:
    """
    Базовый класс, описывающий имущество

    Args:
        worth(float): передается стоимость имущества
    """
    def __init__(self, worth):
        self.worth = worth


class Apartment(Property):
    """
    Класс Квартира. Родитель: Property

    Args:
        worth (float): передается стоимость имущества
    """
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        """
        Геттер для получения налога

        :return: self.worth / 1000
        :rtype: float
        """
        return self.worth / 1000


class Car(Property):
    """
    Класс Машина. Родитель: Property

    Args:
        worth (float): передается стоимость имущества
    """
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        """
        Геттер для получения налога

        :return: self.worth / 200
        :rtype: float
        """
        return self.worth / 200


class CountryHouse(Property):
    """
    Класс Дача. Родитель: Property

    Args:
        worth (float): передается стоимость имущества
    """
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        """
        Геттер для получения налога

        :return: self.worth / 500
        :rtype: float
        """
        return self.worth / 500


print(' ***** Расчет налогов на имущество *****')
amount_money = int(input('Введите количество имеющихся денег: '))
print('Введите стоимость имущества: ')

wroth_1 = float(input('Квартира: '))
tax_apartment = Apartment(wroth_1)
print('Налог на квартиру {}'.format(tax_apartment.tax()))

wroth_2 = float(input('Машина: '))
tax_car = Car(wroth_2)
print('Налог на машину {}'.format(tax_car.tax()))

wroth_3 = float(input('Дача: '))
tax_CountryHouse = CountryHouse(wroth_3)
print('Налог на дачу {}'.format(tax_CountryHouse.tax()))

sum_tax = tax_apartment.tax() + tax_car.tax() + tax_CountryHouse.tax()

if sum_tax < amount_money:
    print('Всего налога на сумму {}, а у вас только {}'.format(sum_tax, amount_money))
    print('Денег не хватает')
else:
    print('Всего налога на сумму {}\nОтлично, денег хватает '.format(sum_tax))
