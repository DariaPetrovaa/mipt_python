class Mother():
    _surname='Ivanova'

    def __str__(self):
        return self.get_self()

    def get_self(self):
        print(self._surname)
        return('Hi,I am mother. And it is my surname.')


class Daughter(Mother):

    def get_self(self):
        print(self._surname)
        return ('And it is daughter and her surname.')


Alice=Mother()
print(Alice)
Gigi=Daughter()
print(Gigi)
#совпадение фамилий-наследование

