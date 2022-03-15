from random import randint, choice


class House:
    food = 50
    money = 0


def repast():
    House.food += 1
    House.money -= 1
    return f'идет в магазин, еда {House.food} деньги {House.money}'


class Person:
    def __init__(self, name):
        self.name = name
        self.satiety = 50

    def eat(self):
        self.satiety += 1
        House.food -= 1
        return f'ест, сытость {self.satiety} еда {House.food}'

    def work(self):
        self.satiety -= 1
        House.money += 1
        return f'работает, сытость {self.satiety} деньги {House.money}'

    def play(self):
        self.satiety -= 1
        return f'играет, сытость {self.satiety}'


person_1 = Person('Вася')
person_2 = Person('Федя')
count = 0

for i in range(365):
    count += 1
    number_cubes = randint(1, 6)
    person = choice([person_1, person_2])
    if person.satiety < 0:
        print(f'К сожалению, {person.name} погиб от голода')
        break
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

print('Выжили!' if count == 365 else 'Все плохо!')
