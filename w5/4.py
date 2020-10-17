class Shape():

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        raise NotImplementedError()

    def print_self(self):
        print('Area is:' , self.get_area())


class Triangle(Shape):

    def get_area(self):
        return 0.5 *self.width * self.height

class Rectangle(Shape):

    def get_area(self):
        return self.width * self.height

tr1 = Triangle(3,5)
rctr1 = Rectangle(3,6)
tr1.print_self()
rctr1.print_self()



