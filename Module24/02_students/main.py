class Student:

    def __init__(self, full_name, group_number, progress):
        self.full_name = full_name
        self.group_number = group_number
        self.progress = progress
        # self.average = average  todo значение не определено

    def give_average(self):  #, progress):  TODO параметр не нужен
        # return self.average == sum(progress) / len(progress)   todo и сравнивать не с чем и не нужно
        return sum(self.progress) / len(self. progress)  # TODO вот так

    def __str__(self):
        return f'{self.full_name} {self.group_number}'

    def good(self):
        good_progress = list(filter(lambda x: x in [4, 5], self.progress))
        return self.progress == good_progress


def receiving_data():
    name = input('ФИ: ')
    group = input('Номер группы: ')
    ball = list(map(int, input('Успеваемость: ').split()))
    return name, group, ball


list_student = [Student(*receiving_data()) for _ in range(2)]
print('список студентов')
for student in list_student:
    print(student)
print()

list_student.sort(key=lambda x: x.give_average())
print('список студентов отсортированный')
for student in list_student:
    print(student)
print()

print('студенты с оценками 4 и 5')
for student in list_student:
    if student.good():
        print(student)

