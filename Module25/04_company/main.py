from random import randint, choice
"""
Модуль random:  генерация случайных данных 
Методы random:
    randint: возвращает случайное число в пределах заданного промежутка
    choice: возвращает список со случайной выборкой из заданной последовательности
"""

Names = ['Алексей', 'Женя', 'Иван', 'Петр', 'Семен', 'Антон', 'Максим']
Surnames = ['Первый', 'Второй', 'Третий', 'Четвертый', 'Пятый']
# TODO имена констант пишутся большими буквами: NAMES


def generate_person():
    """
    Геттер для присваивания работнику имени, фамилии и возраста

    :return: name, surname, age
    :rtype: str
    """
    name = choice(Names)
    surname = choice(Surnames)
    age = randint(20, 50)
    return name, surname, age


class Person:
    """
    Базовый клас описывающий человека

    Args:
        name(str): передает имя человека
        surname(str): передает фамилию человека
        age(int): передает возраст человека
    """
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.amount = 1

    def set_amount(self, amount):
        self.amount = amount

    def __str__(self):
        return f'Меня зовут {self.__name} {self.__surname}. Мой возраст - {self.__age}'


class Employee(Person):
    """
    Класс Работник. Родитель: Person

    """

    def calc_salary(self):
        """
        Геттер для получения расчета зарплаты

        :return: Exception: если метод расчета зарплаты не работает
        """
        raise Exception('Этот метод не работает!')

    def __str__(self):
        return super().__str__() + f'\nМоя зарплата {self.calc_salary()}'


class Manager(Employee):
    """
    Класс Менеджер. Родительский: Employee

    """
    def calc_salary(self):
        """
        Геттер для получения расчета зарплаты

        :return: зарплата менеджера
        """
        return 13000


class Agent(Employee):
    """
    Класс Агент. Родительский: Employee

    """
    def calc_salary(self):
        """
        Геттер для получения расчета зарплаты

        :return: зарплата Агента
        """
        return 5000 + .05 * self.amount


class Worker(Employee):
    """
    Класс Рабочий. Родительский: Employee

    """

    def calc_salary(self):
        """
        Геттер для получения расчета зарплаты

        :return: зарплата рабочего
        """
        return 100 * self.amount


if __name__ == '__main__':
    employees = list()

    for _ in range(3):
        employees.append(Manager(*generate_person()))

    for _ in range(3):
        agent = Agent(*generate_person())
        agent.set_amount(randint(2000, 10000))
        employees.append(agent)

    for _ in range(3):
        worker = Worker(*generate_person())
        worker.set_amount(randint(20, 50))
        employees.append(worker)

    for emp in employees:
        print(emp)
