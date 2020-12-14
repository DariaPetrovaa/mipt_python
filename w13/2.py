

# При сериализации и десериализации не изменяются встроенные функции и классы, самописные классы, изменяются итераторы
#I/O объекты не могут подвергаться сериализации в чистом виде, появляется ошибка cannot pickle '_io.TextIOWrapper' object

import pickle
from collections import deque

class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration

class MyClass:
    def __init__(self, name, surname, is_hired):
        self.name = name
        self.surname = surname
        self.is_hired = is_hired

    def __dict__(self):
        return {'name': self.name, 'surname': self.surname, 'is_hired': self.is_hired}

    def __str__(self):
        return f'MyClass({self.name},{self.surname},{self.is_hired})'


def Serialization(a):
    return pickle.dumps(a)


def Deserialization(a):
    return pickle.loads(a)


a = [SimpleIterator(100),print,deque,deque.copy,MyClass]

for i in a:
    b = Serialization(i)
    c = Deserialization(b)
    if i == c:
        d = 'No'
    else:
        d = 'Yes'
    print(f'Before:{i}\nSerialization:{b}\nAfter:{c}\nDifferent? {d}\n')

with open('text.txt', 'r') as f:
    print(f)
    s = Serialization(f)
    print(s)
    print(Deserialization(s))

