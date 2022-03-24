from random import randint, choice


class CountError(Exception):  # TODO вот так создаются кастомные исключения
    pass


class House:
    food = 50
    money = 0


def repast():
    if House.money > 0:
        House.food += 1
        House.money -= 1
        return f'идет в магазин, еда {House.food} деньги {House.money}'
    else:
        raise ChildProcessError('Закончились деньги!')


class Person:
    def __init__(self, name):
        self.name = name
        self.satiety = 50

    def __str__(self):
        return f'Текущее состояние ребят: \n1) Еда - {House.food} \n2) Сытость - {self.satiety}' \
               f' \n3) Деньги - {House.money}'

    def act(self):
        number_cubes = randint(1, 6)
        if self.satiety < 0:
            raise CountError(f'К сожалению, {self.name} помер с голоду ')
        if self.satiety < 20 and House.food >= 10:
            text = self.eat()
        elif House.food < 10:
            text = repast()
        elif House.money < 50:
            text = self.work()
        elif number_cubes == 1:
            text = self.work()
        elif number_cubes == 2:
            text = self.eat()
        else:
            text = self.play()
        print(self.name, text)

    def eat(self):
        self.satiety += 1
        if House.food > 0:
            House.food -= 1
            return f'ест, сытость {self.satiety} еда {House.food}'
        else:
            raise ChildProcessError('Еды больше нет!')

    def work(self):
        if self.satiety > 0:
            self.satiety -= 1
            House.money += 1
            return f'работает, сытость {self.satiety} деньги {House.money}'
        else:
            raise ChildProcessError('Погибли от голода!')

    def play(self):
        if self.satiety > 0:
            self.satiety -= 1
            return f'играет, сытость {self.satiety}'
        else:
            raise ChildProcessError('Погибли от голода!')


person_1 = Person('Вася')
person_2 = Person('Федя')

for i in range(365):
    Person.act(person_1)
    print(person_1)
    Person.act(person_2)
    print(person_2)

print('Выжили')
