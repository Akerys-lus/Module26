num = int(input('Введите число: '))
flag = True
list_num = []
for n in range(num):
    if n % 2 == 0:
        flag = False
    else:
        list_num.append(n)
print(list_num)
