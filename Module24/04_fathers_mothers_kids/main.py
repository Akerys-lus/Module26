class Parent:
    def __init__(self, name, age, childs):  # TODO Слово "дети" во множественном числе это children, а child не имеет
                                            #  формы множественного числа
        self.name, self.age, self.childs = name, age, childs
        for i_child in [child_info, child_info2]:
            if i_child.age + 16 > self.age:
                raise ValueError('Значение "лет" не подходит к требованиям!')

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
child_info2 = Child('Паша', 8, False, True)
parents_info = Parent('Иван', 30, [child_info, child_info2])

print(parents_info)
