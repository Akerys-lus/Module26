def height(name):
    if name not in list_people:
        return 0
    else:
        return 1 + height(list_people[name])


list_people = {}
for i in range(1, int(input('Введите количество человек: '))):
    (child, parent) = input('{} пара: '.format(i)).split()
    list_people[child] = parent

heights = {}

for people in set(list_people.keys()).union(set(list_people.values())):
    heights[people] = height(people)

print('“Высота” каждого члена семьи:')

for key, value in sorted(heights.items()):
    print(key, value)
