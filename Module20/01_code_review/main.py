students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def func_stud(ready_list):
    lst = []
    string = 0
    for id_stud in ready_list:
        lst += (ready_list[id_stud]['interests'])
        string += len(ready_list[id_stud]['surname'])
    return lst, string


pairs = [(i, students[i]['age']) for i in students]


my_list = func_stud(students)[0]
len_surname = func_stud(students)[1]

print('Список пар "ID студента - Возраст": ', pairs)
print('Полный список интересов всех студентов: ', my_list)
print('Общая длина всех фамилий студентов: ', len_surname)
