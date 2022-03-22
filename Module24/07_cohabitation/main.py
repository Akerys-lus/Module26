from random import randint, choice


class House:
    food = 50
    money = 0


def repast():
    if House.money > 0:
        House.food += 1
        House.money -= 1
        return f'идет в магазин, еда {House.food} деньги {House.money}'
    else:
        raise CountError('Закончились деньги!')


class Person:
    def __init__(self, name):
        self.name = name
        self.satiety = 50

    def eat(self):
        self.satiety += 1
        if House.food > 0:
            House.food -= 1
            return f'ест, сытость {self.satiety} еда {House.food}'
        else:
            raise CountError('Еды больше нет!')

    def work(self):
        if self.satiety > 0:
            self.satiety -= 1
            House.money += 1
            return f'работает, сытость {self.satiety} деньги {House.money}'
        else:
            raise CountError('Погибли от голода!')

    def play(self):
        if self.satiety > 0:
            self.satiety -= 1
            return f'играет, сытость {self.satiety}'
        else:
            raise CountError('Погибли от голода!')


person_1 = Person('Вася')
person_2 = Person('Федя')


def test_life(person):
    number_cubes = randint(1, 6)
    if person.satiety < 0:
        raise CountError(f'К сожалению, {person.name} помер с голоду ')
    if person.satiety < 20 and House.food >= 10:
        text = person.eat()
    elif House.food < 10:
        text = repast()
    elif House.money < 50:
        text = person.work()
    elif number_cubes == 1:
        text = person.work()
    elif number_cubes == 2:
        text = person.eat()
    else:
        text = person.play()
    print(person.name, text)


for i in range(365):
    test_life(person_1)
    test_life(person_2)
    if i == 364:
        print('Выжили')

