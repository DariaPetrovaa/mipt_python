class Vector:

    def __init__(self, a):
        if type(a) is list:
            a = "".join(map(str,a))
        x, y, z = a.split(',')
        x = int(x)
        y = int(y)
        z = int(z)
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        a1 = self.x + other.x
        a2 = self.y + other.y
        a3 = self.z + other.z
        ans = self.formatir(a1,a2,a3)
        return Vector(ans)

    def __sub__(self, other):
        a1 = self.x - other.x
        a2 = self.y - other.y
        a3 = self.z - other.z
        ans = self.formatir(a1,a2,a3)
        return Vector(ans)
       
    def __and__(self, other):
        a1 = self.y*other.z - other.y*self.z
        a2 = other.x*self.z - self.x*other.z
        a3 = self.x*other.y - self.y*other.x
        ans = self.formatir(a1,a2,a3)
        return Vector(ans) 
     
    def formatir(self,a1,a2,a3):
        ans = a1,a2,a3
        ans = str(ans)
        ans = ans[:0] + ans[1:-1]
        ans = str(ans)
        return ans

    def distance(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __str__(self): 
        return f"Вектор имеет координаты {self.x, self.y, self.z}"
