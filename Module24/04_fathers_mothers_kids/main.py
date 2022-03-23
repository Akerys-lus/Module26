class Parent:
    def __init__(self, name, age, childs):
        # TODO Именно тут надо проитерировать по списку объектов детей и проверить допустимость их возраста
        self.name, self.age, self.childs = name, age, childs

    def __str__(self):
        return self.name + ' ' + str(self.age) + '\n' + \
               '\n'.join([str(i) for i in self.childs])

    def calm(self, child):
        for i in self.childs:
            if i in child:
                i.is_calm = True

    def feed(self, child):
        for i in self.childs:
            if i in child:
                i.is_feed = True


class Child:
    def __init__(self, name, age, is_calm, is_feed):
        self.name, self.age, self.is_calm, self.is_feed = \
            name, age, is_calm, is_feed

    def __str__(self):
        return self.name + ' ' + str(self.age) + ' лет ' + \
               ('Спокоен ' if self.is_calm else 'Раздражен ') + \
               ('Сыт ' if self.is_feed else 'Голоден ')


child_info = Child('Саша', 7, True, False)
parents_info = Parent('Иван', 30, [child_info])
if child_info.age + 16 < parents_info.age:  # TODO эта логика должна быть в классе Родитель (с циклом по списку детей)
    print(parents_info)
else:
    raise ValueError('Не правильно указан возраст!')
