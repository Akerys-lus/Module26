a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
while a < b:
    for i in range(4):
        if 3 == str(a).count(str(i)):
            print(a)
    a += 1
