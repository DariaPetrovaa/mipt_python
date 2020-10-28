from math import sin,sqrt
import cmath

class MyMath:
    pi = 3.14
    _complex = False #инкапсуляция  


    @staticmethod
    def get_sin(x):  #наследование, get_sin не реализован в дочернем классе, но мы можем его вызвать, как и get_sqrt
        return sin(x)

    @classmethod
    def get_sqrt(cls,x):  #наследование
        if not cls._complex: #полиморфизм
            if x>=0:
                return sqrt(x)
            else: 
                return ValueError('Было введено отрицательное число')
        else:
            ans = cmath.sqrt(x)
            return ans.real, ans.imag

class MyComplexMath(MyMath): #наследование
    _complex = True  #инкапсуляция 

