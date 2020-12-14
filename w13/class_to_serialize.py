import json

class MyClass:
    def __init__(self, name, surname, is_hired):
        self.name = name
        self.surname = surname
        self.is_hired = is_hired

    def __dict__(self):
        return {'name': self.name, 'surname': self.surname, 'is_hired': self.is_hired}

    def __str__(self):
        return f'MyClass({self.name},{self.surname},{self.is_hired})'


def obj_to_json(obj):
    data = obj.__dict__()
    return json.dumps(data)


def json_to_obj(obj):
    return MyClass(**json.loads(obj))

a = MyClass('my_name', 'my_surname', True)
b = obj_to_json(a)
print(b,type(b))

c = json_to_obj(b)
print(c,type(c))
