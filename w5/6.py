class Animal():
    name=''
    age=0

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.get_self()


class Zebra(Animal):

    def __init__(self, name, age, colour):
        super().__init__(name,age)
        self.colour = colour

    def get_self(self):
        return " ".join(str(x) for x in [" I am a zebra",'\n',
            "Name:",self.name, '\n',
            "Age:" , self.age, '\n',
            "Colour:", self.colour, '\n'])


class Dolphin(Animal):

    def __init__(self, name, age, mood):
        super().__init__(name,age)
        self.mood = mood

    def get_self(self):
        return " ".join(str(x) for x in [" I am a dolphin",'\n',
            "Name:",self.name, '\n',
            "Age:" , self.age, '\n',
            "Mood:", self.mood, '\n'])

a1 = Zebra('Martin', 15, 'black_and_white')
a2 = Dolphin('Bernie', 18, 'great')
print(a1)
print(a2)
