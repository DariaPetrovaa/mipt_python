import math
from my_mathematics.math import MyMath
import cmath
from my_mathematics.math import MyComplexMath
import numpy as np
from my_mathematics.linear_algebra import Vector

def test_sin():
    assert MyMath.get_sin(2) == math.sin(2)
    assert MyMath.get_sin(-2) == math.sin(-2)
    assert MyMath.get_sin(0) == math.sin(0)

def test_sqrt():
    assert MyMath.get_sqrt(3) == math.sqrt(3)
    assert MyMath.get_sqrt(0) == math.sqrt(0)
    #assert MyMath.get_sqrt(-3) == math.sqrt(-3)    

def test_complex():
    assert MyComplexMath.get_sqrt(3+4j) == (cmath.sqrt(3+4j).real, cmath.sqrt(3+4j).imag)
    assert MyComplexMath.get_sqrt(3-4j) == (cmath.sqrt(3-4j).real, cmath.sqrt(3-4j).imag)
    assert MyComplexMath.get_sqrt(-3+4j) == (cmath.sqrt(-3+4j).real, cmath.sqrt(-3+4j).imag)
    assert MyComplexMath.get_sqrt(-4j) == (cmath.sqrt(-4j).real, cmath.sqrt(-4j).imag)
    assert MyComplexMath.get_sqrt(3j) == (cmath.sqrt(3j).real, cmath.sqrt(3j).imag)   # assert MyComplexMath.get_sqrt(-3+4j) == (cmath.sqrt(-3+4j).real, cmath.sqrt(-3+4j).imag)




def test_distance():
    v1 = Vector('3,4,5')
    assert Vector.distance(v1) == np.linalg.norm([3,4,5]) 
    v2 = Vector('3,4,0')
    assert Vector.distance(v2) == np.linalg.norm([3,4,0])
    v3 = Vector('3,0,5')
    assert Vector.distance(v3) == np.linalg.norm([3,0,5])
    v4 = Vector('0,4,5')
    assert Vector.distance(v4) == np.linalg.norm([0,4,5])
    v5 = Vector('3,0,0')
    assert Vector.distance(v5) == np.linalg.norm([3,0,0])
    v6 = Vector('0,0,0')
    assert Vector.distance(v6) == np.linalg.norm([0,0,0])
    v7 = Vector('-3,-4,5')
    assert Vector.distance(v7) == np.linalg.norm([-3,-4,5])
    v8 = Vector('-3.7,-4,5')
    assert Vector.distance(v8) == np.linalg.norm([-3.7,-4,5])
    v9 = Vector('-3.7,-4,0')
    assert Vector.distance(v9) == np.linalg.norm([-3.7,-4,0])
    v10 = Vector('3.7,4.6,5.9')
    assert Vector.distance(v10) == np.linalg.norm([3.7,4.6,5.9])

def test_add():
    v1 = Vector('3,4,5')
    v2 = Vector ('-2,6,7')
    numpy_array_1 = np.array([3,4,5])
    numpy_array_2 = np.array([-2,6,7])
    ans1 = v1 + v2
    ans2 = numpy_array_1 + numpy_array_2
    assert ans1.x == ans2[0] 
    assert ans1.y == ans2[1]
    assert ans1.z == ans2[2]

    v1 = Vector('3.3,-4.6,0')
    v2 = Vector ('-2,0,7.4')
    numpy_array_1 = np.array([3.3,-4.6,0])
    numpy_array_2 = np.array([-2,0,7.4])
    ans1 = v1 + v2
    ans2 = numpy_array_1 + numpy_array_2
    assert ans1.x == ans2[0] 
    assert ans1.y == ans2[1]
    assert ans1.z == ans2[2]


def test_sub():
    v1 = Vector('3,4,5')
    v2 = Vector ('-2,6,7')
    numpy_array_1 = np.array([3,4,5])
    numpy_array_2 = np.array([-2,6,7])
    ans1 = v1 - v2
    ans2 = numpy_array_1 - numpy_array_2
    assert ans1.x == ans2[0] 
    assert ans1.y == ans2[1]
    assert ans1.z == ans2[2]

    v1 = Vector('-3,0,5.8')
    v2 = Vector ('0,6,-7.8')
    numpy_array_1 = np.array([-3,0,5.8])
    numpy_array_2 = np.array([0,6,-7.8])
    ans1 = v1 - v2
    ans2 = numpy_array_1 - numpy_array_2
    assert ans1.x == ans2[0] 
    assert ans1.y == ans2[1]
    assert ans1.z == ans2[2]
    

def test_and():
    v1 = Vector('3,4,5')
    v2 = Vector ('-2,6,7')
    numpy_array_1 = np.array([3,4,5])
    numpy_array_2 = np.array([-2,6,7])
    ans1 = v1 &  v2
    ans2 = np.cross(numpy_array_1,numpy_array_2)
    assert ans1.x == ans2[0]
    assert ans1.y == ans2[1]
    assert ans1.z == ans2[2]

    v1 = Vector('0,4,0')
    v2 = Vector ('-2,0,7')
    numpy_array_1 = np.array([0,4,0])
    numpy_array_2 = np.array([-2,0,7])
    ans1 = v1 &  v2
    ans2 = np.cross(numpy_array_1,numpy_array_2)
    assert ans1.x == ans2[0]
    assert ans1.y == ans2[1]
    assert ans1.z == ans2[2]

    v1 = Vector('3.8,4,5')
    v2 = Vector ('-2,-6.9,7')
    numpy_array_1 = np.array([3.8,4,5])
    numpy_array_2 = np.array([-2,-6.9,7])
    ans1 = v1 &  v2
    ans2 = np.cross(numpy_array_1,numpy_array_2)
    assert ans1.x == ans2[0]
    assert ans1.y == ans2[1]
    assert ans1.z == ans2[2]


    











    
