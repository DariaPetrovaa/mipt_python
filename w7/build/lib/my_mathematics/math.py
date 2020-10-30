from math import sin,sqrt

class MyMath:
    pi = 3.14
    _complex = False #инкапсуляция  


    @staticmethod
    def get_sin(x):  #наследование, get_sin не реализован в дочернем классе, но мы можем его вызвать, как и get_sqrt
        return sin(x)

    @classmethod
    def get_sqrt(cls,x):  #наследование
        if x>=0:
            return sqrt(x)
        else:
            if not cls._complex: #полиморфизм
                return ValueError('Было введено отрицательное число')
            else:
                return (0, sqrt(-x)*1.0j)

class MyComplexMath(MyMath): #наследование
    _complex = True  #инкапсуляция 

