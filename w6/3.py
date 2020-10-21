from math import sin,sqrt


class MyMath:
    pi = 3.14
    _complex = False #инкапсуляция  

  # @classmethod
   # def get_complex(cls):
    #    return cls.__complex

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

    #@classmethod
    #def get_complex(cls):
    #    return cls.__complex

a = MyMath()
b = MyComplexMath()
print(a.get_sqrt(-1))
print(b.get_sqrt(-1))

#Мы использовали классический метод, так как он может получать доступ или менять состояние класса, а статистический - нет (поле _complex)
