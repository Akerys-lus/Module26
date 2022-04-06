import random

"""
Модуль random:  генерации случайных данных
"""


def pollution():
    House.dirt += 5


class House:
    """
    Базовый класс, описывающий дом

    Args:
        family (list): список с именами жильцов

    Attributes:
        many (int): передает кол-во денег
        food (int): передает кол-во еды
        cat_food (int): передает кол-во еды для кота
        dirt (int): передает кол-во грязи в доме
        fur_coat (int): передает кол-во купленных шуб
        earned (int): передает кол-во заработанных денег
        food_eaten (int): передает кол-во съеденной еды
        cat_eat (int): передает кол-во еды, съеденной котом
    """
    many = 100
    food = 50
    cat_food = 30
    dirt = 0
    fur_coat = 0
    earned = 0
    food_eaten = 0
    cat_eat = 0

    def __init__(self, family):
        self.family = family


class Residents:
    """
    Базовый класс, описывающий имена, сытость и величину счастья жильцов(каждого жильца отдельно)

    Args:
        name (str): передает имя
        satiety (int): передает величину сытости
        happiness (int): передает величину счастья
    """

    def __init__(self, name=None, satiety=None, happiness=None):
        self.name = name
        self.satiety = satiety
        self.happiness = happiness

    def eat(self):
        self.satiety += 30
        House.food -= 30


class Husband(Residents):
    """
    Класс Муж. Родитель Residents

    Args:
        name (str): передает имя мужа
        satiety (int): передает величину сытости мужа
        happiness (int): передает величину счастья мужа
        work (int): передает кол-во денег за работу мужа
    """

    def __init__(self, name, satiety=30, happiness=100, work=150):
        super().__init__(name, satiety, happiness)
        self.work = work

    def work_day(self):
        House.many += self.work
        self.satiety -= 10
        print('Работа')

    def petting_cat(self):
        self.happiness += 5
        self.satiety -= 10

    def game(self):
        self.happiness += 20
        self.satiety -= 10

    def act(self):
        if House.many <= 150:
            husband.work_day()
            print('Экстренная работа')
            House.earned += 150
        elif husband.happiness <= 50:
            husband.game()
            print('Расслабляется')
        elif husband.happiness <= 70:
            husband.petting_cat()
            print('Гладит кота')
        else:
            husband.work_day()
            print('Обычная работа')
            House.earned += 150
        if House.dirt >= 90:
            i_resident.happiness -= 10
        elif House.food >= 60 and self.satiety <= 30:
            Residents.eat(self)
            print(self.name, 'поел')
            House.food_eaten += 30


def buy_food():
    House.many -= 100
    House.food += 100


def buy_cat_food():
    House.many -= 50
    House.cat_food += 50


class Wife(Residents):
    """
    Класс Жена. Родитель: Residents

    Args:
        name (str): передает имя жены
        satiety (int): передает величину сытости жены
        happiness (int): передает величину счастья жены
    """

    def __init__(self, name, satiety=30, happiness=100):
        super().__init__(name, satiety, happiness)

    def petting_cat(self):
        self.happiness += 5
        self.satiety -= 10

    def purchase(self):
        House.many -= 350
        self.happiness += 60
        self.satiety -= 10

    def cleaning(self):
        House.dirt -= 100
        self.satiety -= 10

    def act(self):
        if House.food <= 60 and House.many > 100:
            buy_food()
        elif House.cat_food <= 20:
            buy_cat_food()
        elif House.dirt >= 50:
            wife.cleaning()
            print("Уборка")
        elif wife.happiness <= 70:
            wife.petting_cat()
            print('Гладит кота')
        elif House.many > 450:
            wife.purchase()
            print('Покупка шубы')
            House.fur_coat += 1
        else:
            wife.petting_cat()
            print('Гладит кота')
        if House.food >= 60 and self.satiety <= 30:
            Residents.eat(self)
            print(self.name, 'поела')
            House.food_eaten += 30


def shitting():
    House.dirt += 5


class Cat(Residents):
    """
    Класс Кот. Родитель: Residents

    Args:
        name (str): передает имя кота
        satiety (int): передает величину сытости кота
    """

    def __init__(self, name, satiety=30):
        super().__init__(name, satiety)

    def eat(self):
        self.satiety += 20
        House.cat_food -= 10

    def act(self):
        if House.cat_food >= 20 <= self.satiety:
            cat.eat()
            print('Кот поел')
            House.cat_eat += 10
        if random.randint(1, 2) == 1:
            House.dirt += 5
            print('Кот содрал обои')
        else:
            cat.satiety -= 10
            print('Кот спит')


def life_dead(family):
    """
    Геттер при смерти одного из жильцов, либо от голода, либо от депрессии

    :param family: список жильцов
    :rtype: list
    :return: True если кто-нибудь погиб, если нет, то Else
    """
    for i_elem in family:
        if i_elem.satiety <= 0:
            print('1 из жильцов умер от голода')
            return True
        elif i_elem.happiness == 0 and not isinstance(i_elem, Cat):
            print('1 из жильцов умер от депрессии')
            return True
        else:
            return False


husband = Husband('Гейб')
wife = Wife('Маша')
cat = Cat('Барсик')
family_list = [husband, wife, cat]
house = House(family_list)
for i_day in range(1, 365):
    print(f'день {i_day}')
    pollution()
    if life_dead(family_list):
        print('Эксперимент не удался.')
        break
    elif i_day == 365:
        print(f'\nBce живы')
        break
    else:
        husband.act()
        wife.act()
        cat.act()
print(f'\nЗа год: \nКуплено шуб: {House.fur_coat}' f'\nЗаработано: {House.earned}'
      f' \nСъедено: {House.food_eaten}\nКот съел: {House.cat_eat}')

