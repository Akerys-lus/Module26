count_containers = int(input('Введите кол-во контейнеров: '))
all_container = []
count = 0
for i in range(count_containers):
    container = float(input('Введите массу контейнера(от большего к меньшему): '))
    if container <= 200 and (container % 1) == 0:
        all_container.append(container)
    else:
        print('Ошибка ввода значения, попробуйте ещё раз. ')
        container = float(input('Введите массу контейнера(от большего к меньшему): '))

new_container = int(input('Введите массу нового контейнера: '))

while count < len(all_container) and all_container[count] >= new_container:
    count += 1
print('\nНомер, куда встанет контейнер:', count + 1)