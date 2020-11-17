import pytest
import math
from my_mathematics.math import MyMath
import cmath
from my_mathematics.math import MyComplexMath
import numpy as np
from my_mathematics.linear_algebra import Vector

@pytest.mark.parametrize("test_input, expected_result", [(2,math.sin(2)),(-2,math.sin(-2)),(0, math.sin(0))])
def test_sin(test_input, expected_result):
    assert MyMath.get_sin(test_input) == expected_result

@pytest.mark.parametrize("test_input, expected_result", [(3,math.sqrt(3)),(0,math.sqrt(0))])
def test_sqrt(test_input, expected_result):
    assert MyMath.get_sqrt(test_input) == expected_result

@pytest.mark.parametrize("test_input, expected_result", [(3+4j,(cmath.sqrt(3+4j).real,cmath.sqrt(3+4j).imag)),(3-4j,(cmath.sqrt(3-4j).real,cmath.sqrt(3-4j).imag)), (-3+4j,(cmath.sqrt(-3+4j).real,cmath.sqrt(-3+4j).imag)), (-4j,(cmath.sqrt(-4j).real,cmath.sqrt(-4j).imag)), (3j,(cmath.sqrt(3j).real,cmath.sqrt(3j).imag))])
def test_complex(test_input, expected_result):
    assert MyComplexMath.get_sqrt(test_input) == expected_result

@pytest.mark.parametrize("test_input, expected_result", [(Vector('3,4,5'),np.linalg.norm([3,4,5])), (Vector('3,4,0'),np.linalg.norm([3,4,0])), (Vector('3,0,5'),np.linalg.norm([3,0,5])), (Vector('0,4,5'),np.linalg.norm([0,4,5])), (Vector('3,0,0'),np.linalg.norm([3,0,0])), (Vector('0,0,0'),np.linalg.norm([0,0,0])), (Vector('-3,-4,5'),np.linalg.norm([-3,-4,5])), (Vector('-3.7,-4,5'),np.linalg.norm([-3.7,-4,5])), (Vector('-3.7,-4,0'),np.linalg.norm([-3.7,-4,0])),(Vector('3.7,4.6,5.9'),np.linalg.norm([3.7,4.6,5.9]))])
def test_distance(test_input, expected_result):
    assert Vector.distance(test_input) == expected_result

@pytest.mark.parametrize("test_input, expected_result", 
[((Vector('3,4,5')+Vector ('-2,6,7')).x,(np.array([3,4,5])+np.array([-2,6,7]))[0]),((Vector('3,4,5')+Vector ('-2,6,7')).y, (np.array([3,4,5])+np.array([-2,6,7]))[1]),((Vector('3,4,5')+Vector ('-2,6,7')).z, (np.array([3,4,5])+np.array([-2,6,7]))[2]),((Vector('3.3,-4.6,0')+Vector ('-2,0,7.4')).x,(np.array([3.3,-4.6,0])+np.array([-2,0,7.4]))[0]),
((Vector('3.3,-4.6,0')+Vector ('-2,0,7.4')).y,(np.array([3.3,-4.6,0])+np.array([-2,0,7.4]))[1]),
((Vector('3.3,-4.6,0')+Vector ('-2,0,7.4')).z,(np.array([3.3,-4.6,0])+np.array([-2,0,7.4]))[2])])
def test_add(test_input, expected_result):   
    assert test_input == expected_result 

@pytest.mark.parametrize("test_input, expected_result", 
[((Vector('3,4,5')-Vector ('-2,6,7')).x,(np.array([3,4,5])-np.array([-2,6,7]))[0]),((Vector('3,4,5')-Vector ('-2,6,7')).y, (np.array([3,4,5])-np.array([-2,6,7]))[1]),((Vector('3,4,5')-Vector ('-2,6,7')).z, (np.array([3,4,5])-np.array([-2,6,7]))[2]),((Vector('-3,-0,5.8')-Vector ('0,6,-7.8')).x,(np.array([-3,0,5.8])-np.array([0,6,-7.8]))[0]),
((Vector('-3,0,5.8')-Vector ('0,6,-7.8')).y,(np.array([-3,0,5.8])-np.array([0,6,-7.8]))[1]),
((Vector('-3,0,5.8')-Vector ('0,6,-7.8')).z,(np.array([-3,0,5.8])-np.array([0,6,-7.8]))[2])])
def test_sub(test_input,expected_result):
    assert test_input == expected_result 

@pytest.mark.parametrize("test_input, expected_result", 
[((Vector('3,4,5') & Vector ('-2,6,7')).x,(np.cross(np.array([3,4,5]),np.array([-2,6,7])))[0]),((Vector('3,4,5') & Vector ('-2,6,7')).y, (np.cross(np.array([3,4,5]),np.array([-2,6,7])))[1]),((Vector('3,4,5') & Vector ('-2,6,7')).z, (np.cross(np.array([3,4,5]),np.array([-2,6,7])))[2]),((Vector('-3,-0,5.8') & Vector ('0,6,-7.8')).x,(np.cross(np.array([-3,0,5.8]),np.array([0,6,-7.8])))[0]),
((Vector('-3,0,5.8') & Vector ('0,6,-7.8')).y,(np.cross(np.array([-3,0,5.8]),np.array([0,6,-7.8])))[1]),
((Vector('-3,0,5.8') & Vector ('0,6,-7.8')).z,(np.cross(np.array([-3,0,5.8]),np.array([0,6,-7.8])))[2])])
def test_and(test_input, expected_result):
    assert test_input == expected_result 


  

    











    
