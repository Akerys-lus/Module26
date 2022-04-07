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

    def move(self, new_dist):
        """
        Геттер для перемещения автомобиля

        :param new_dist: кол-во км. которое проедет автобус
        :rtype: float
        :raise ValueError: если величина перемещения автомобиля отрицательная
        """
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
        return f'Автобус проехал - {self.dist} км. \nВодитель заработал - {self.all_money} р.' \
               f' \nКол-во пассажиров - {self.filled_places} чел.\nАвтобус, в настоящее время находиться' \
               f'в точке (х:{self.x}, у:{self.y}).'

    def move(self, new_dist):
        """
        Геттер для перемещения автомобиля

        :raise ValueError: если величина перемещения автомобиля отрицательная
        :raise Exception: если введено что-то кроме (yes, no, no_changes)
        """
        if new_dist < 0:
            raise ValueError('Введено неправильное значение!')

        self.x = self.x + new_dist * math.cos(self.fi)
        self.y = self.y + new_dist * math.sin(self.fi)
        self.dist += new_dist
        # TODO Повторно: вызовите метод базового класса super().move(new_dist) чтобы не дублировать код расчёта
        #  новых координат

        self.all_money += self.filled_places * new_dist * self.fare

    def to_come_in(self, passengers):
        """
        Геттер для увеличения числа пассажиров

        :param passengers: кол-во пассажиров
        :rtype: int
        :raise ValueError: введено неверное число пассажиров
        """
        if passengers > self.filled_places - self.free_places:
            self.free_places -= passengers
            self.filled_places += passengers
        else:
            raise ValueError('Указано неверное число пассажиров!')

    def go_out(self, passengers):
        """
        Геттер для уменьшения числа пассажиров

        :param passengers: кол-во пассажиров
        :rtype: int
        :raise ValueError: введено неверное число пассажиров
        """
        if passengers > self.filled_places - self.free_places:
            self.free_places += passengers
            self.filled_places -= passengers
        else:
            raise ValueError('Указано неверное число пассажиров!')


Auto = Automobile(3, 4, 90)
Buss = Bus(10, 10, 10)

new_distance = float(input('Сколько км. проехал автомобиль?: '))
if new_distance < 0:
    raise Exception('Автомобиль не может проехать отрицательное кол-во км.')
Auto.move(new_distance)
print(Auto)

count_stop = int(input('Сколько остановок проедет автобус?: '))
for i_stop in range(count_stop):
    question = input('Пассажиры вошли или вышли(yes/no)?: ')
    new_dist_bus = float(input('Сколько км. проехал автобус?: '))
    if question == 'yes':
        passengers_bus = int(input('Сколько пассажиров вошло?: '))
        Buss.to_come_in(passengers_bus)
    elif question == 'no':
        passengers_bus = int(input('Сколько пассажиров вышло?: '))
        Buss.go_out(passengers_bus)
    else:
        raise Exception('Ошибка ввода.')
    Buss.move(new_dist_bus)
    print(Buss)

