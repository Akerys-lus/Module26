cell_efficiency = [3, 0, 6, 2, 10]
cell_check = []
print('Кол-во клеток: ', len(cell_efficiency) - 1)
for i in range(len(cell_efficiency)):
    if i > cell_efficiency[i]:
        cell_check.append(cell_efficiency[i])
print('Неподходящие значения:', cell_check)