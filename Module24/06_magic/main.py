class Element:

    def __init__(self, elem):
        if elem in ("Вода", "Воздух", "Огонь", "Земля", "Шторм", "Грязь", "Пыль", "Лава", "Молния", "Пар"):
            self.name = elem
        else:
            raise ValueError

    def __repr__(self):
        return "§<" + self.name + ">§"

    def __add__(self, other):
        if {self.name, other.name} == {"Вода", "Воздух"}:
            return Element("Шторм")
        if {self.name, other.name} == {"Вода", "Огонь"}:
            return Element("Пар")
        if {self.name, other.name} == {"Вода", "Земля"}:
            return Element("Грязь")
        if {self.name, other.name} == {"Воздух", "Огонь"}:
            return Element("Молния")
        if {self.name, other.name} == {"Воздух", "Земля"}:
            return Element("Пыль")
        if {self.name, other.name} == {"Огонь", "Земля"}:
            return Element("Лава")
        raise ValueError


elem1, elem2 = input('Введите 2-а вида стихий из возможных(Вода, Огонь, Земля, Воздух): ').strip().split(' ')
sum_elem = Element(elem1) + Element(elem2)

print(elem1, "+", elem2, "=", sum_elem)

# TODO Заданием предусматривалось создание классов для каждого элемента, а принадлежность объекта классу должно
#  определяться не сравнениями строковых атрибутов классов, а единственно надёжным способом - c помощью функции
#  isinstance
