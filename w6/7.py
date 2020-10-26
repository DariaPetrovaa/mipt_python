from math import sqrt

#Координаты вектора вводятся в виде строки "x,y,z"
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

N=int(input())
points_list = [[0]*3 for _ in range(N)]

for i in range(N):
    a = input()
    a = ', '.join(list(a.split(',')))
    points_list[i]=a
ans  = 0
for i in range(N):
    b = Vector(points_list[i])
    dist = b.distance()
    if dist > ans:
        ans = dist
        point = points_list[i]
print('Наиболее дальняя точка имеет координаты', point, ". Расстояние от этой точки до начала координат", ans, '.')

A = Vector('2,4,5')
B=Vector('3,56,7')
C = A - B
print(str(C))
C = A + B
print(str(C))
C = A & B
print(str(C))
