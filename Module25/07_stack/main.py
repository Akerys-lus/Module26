class Stack:
    """
    Базовый класс реализации Стека

    Attributes:
        stack (list): список элементов, передающихся в стек
    """
    def __init__(self):
        self.stack = []

    def __str__(self):
        return f'{self.stack}'

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed


class TaskManager:
    """
    Базовый класс описывающий диспетчер задач

    Attributes:
        stack (dict): словарь стека
        sorted_tuple (dict): словарь для сортировки
        results (str): строка для визуализации результата сортировки словаря
    """
    def __init__(self):
        self.stack = dict()
        self.sorted_tuple = {}
        self.results = 'Результат:\n'

    def __str__(self):
        for i_elem in self.sorted_tuple:
            self.results += str(i_elem[0]) + ' ' + i_elem[1] + '\n'
        return f'{self.results}'

    def push(self, key, value):
        if key in self.stack:
            self.stack[key] += '; ' + value
        else:
            self.stack[key] = value

    def new_task(self, task, priority):
        TaskManager.push(self, priority, task)
        TaskManager.stack_sorted(self)

    def stack_sorted(self):
        self.sorted_tuple = sorted(self.stack.items(), key=lambda x: x[0])


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
