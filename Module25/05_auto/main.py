import math


class Automobile:
    """
    Базовый класс описывающий движения автомобиля

    Args:
        x (float): передает координату по оси Ох
        y (float): передает координату по оси Оу
        fi (float): передает направление автомобиля в градусах
        dist (float): передает дистанцию, которую проедет автомобиль
    """

    def __init__(self, x, y, fi, dist=0):
        self.x, self.y, self.fi, self.dist = x, y, fi, dist

    def __str__(self):
        return f'Автомобиль проехал {self.dist}км.' \
               f'\nАвтомобиль, в настоящее время, расположен в точке (х:{self.x}, у:{self.y}).'

    def move(self):
        """
        Геттер для перемещения автомобиля

        Attributes:
            new_dist (float): пользователь вводит кол-во км. которые проедет автомобиль
        """
        new_dist = float(input('Сколько км. проехал автомобиль?: '))  # TODO более практично с точки зрения дальнейшего
        # переиспользования класса, не привязывать код класса к конкретному вводу/выводу (тут - к консоли), тогда класс
        # можно использовать и в проектах с другим интерфейсом. Запросит нужные данные у пользователя в основном коде
        # программы, а методу передавайте это значение через параметр
        if new_dist < 0:
            raise ValueError('Введено неправильное значение!')
        self.x = self.x + new_dist * math.cos(self.fi)
        self.y = self.y + new_dist * math.sin(self.fi)
        self.dist += new_dist


class Bus(Automobile):
    def __init__(self, x, y, fi, dist=0, filled_places=0, free_places=25, all_money=0, fare=10):
        self.filled_places, self.free_places, self.all_money, self.fare, self.dist \
            = filled_places, free_places, all_money, fare, dist
        super().__init__(x, y, fi)

    def __str__(self):
        return f'Автобус проехал {self.dist} км. \nВодитель заработал {self.all_money} р.' \
               f' \nКол-во пассажиров - {self.filled_places}.\nАвтобус, в настоящее время находиться' \
               f'в точке (х:{self.x}, у:{self.y}).'

    def move(self):
        """
        Геттер для перемещения автомобиля

        Attributes:
        new_dist (float): пользователь вводит кол-во км. которые проедет автомобиль
        question (str): пользователь может изменить кол-во пассажиров(yes - увеличить,
            no - уменьшить, no_changes - не изменять)
        money (float): кол-во денег полученных с пассажиров за проезд

        :raise ValueError: если величина перемещения автомобиля отрицательная
        :raise Exception: если введено что-то кроме (yes, no, no_changes)
        """
        new_dist = float(input('Сколько км. проехал автобус?: '))  # TODO Аналогично предыдущему
        if new_dist < 0:
            raise ValueError('Введено неправильное значение!')
        self.x = self.x + new_dist * math.cos(self.fi)
        self.y = self.y + new_dist * math.sin(self.fi)
        self.dist += new_dist
        # TODO чтобы не дублировать код расчёта новых координат - вызовите метод базового класса (используйте super())
        question = input('Пассажиры вошли или вышли(yes/no/no_changes)?: ')  # TODO зачем это в методе "перемещение"?
        # Нужно только расчитать стоимость провоза имеющихся пассажирова на заданное расстояние и увеличить значение
        # атрибута self.all_money
        if question == 'yes':
            Buss.to_come_in(new_dist)
        elif question == 'no':
            Buss.go_out(new_dist)
        elif question == 'no_changes':
            money = self.filled_places * new_dist * self.fare
            self.all_money += money
        else:
            raise Exception('Ошибка ввода.')

    def to_come_in(self, new_dist):
        """
        Геттер для увеличения числа пассажиров

        Attributes:
            passengers (int): кол-во пассажиров
            money (float): кол-во полученных водителем денег

        :param new_dist: кол-во км. которое проедет автобус
        :rtype: float
        :raise ValueError: введено неверное число пассажиров
        """
        passengers = int(input('Сколько людей зашло в автобус?: '))
        if passengers > self.filled_places - self.free_places:
            self.free_places -= passengers
            self.filled_places += passengers
            money = self.filled_places * new_dist * self.fare
            self.all_money += money
        else:
            raise ValueError('Указано неверное число пассажиров!')

    def go_out(self, new_dist):
        """
        Геттер для уменьшения числа пассажиров

        Attributes:
            passengers (int): кол-во пассажиров
            money (float): кол-во полученных водителем денег

        :param new_dist: кол-во км. которое проедет автобус
        :rtype float
        :raise ValueError: введено неверное число пассажиров
        """
        passengers = int(input('Сколько людей вышло из автобуса?: '))
        if passengers > self.filled_places - self.free_places:
            self.free_places += passengers
            self.filled_places -= passengers
            money = self.filled_places * new_dist * self.fare
            self.all_money += money
        else:
            raise ValueError('Указано неверное число пассажиров!')


Auto = Automobile(3, 4, 90)
Buss = Bus(10, 10, 10)

Auto.move()
print(Auto)
Buss.move()
print(Buss)
Buss.move()
print(Buss)
