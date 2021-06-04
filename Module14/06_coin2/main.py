import math

print("Введите координаты точки и радиус круга")
x = float(input("Введите х: "))
y = float(input("Введите y: "))
r_circle = float(input("Введите радиус: "))

hypotenuse = math.sqrt(x ** 2 + y ** 2)

if hypotenuse <= r_circle:
    print("Монетка где-то рядом.")
else:
    print("Монетки нет поблизости.")