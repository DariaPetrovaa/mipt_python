import pytest
from tasks.task_3 import analogue_zip, analogue_map, analogue_enumerate
import math

def test_zip(some_data_1,some_data_2,some_data_3):
    for pair in zip(analogue_zip(some_data_1),zip(some_data_1)):
        assert pair[0] == pair[1]
    for pair in zip(analogue_zip(some_data_2),zip(some_data_2)):
        assert pair[0] == pair[1]
    for pair in zip(analogue_zip(some_data_3),zip(some_data_3)):
        assert pair[0] == pair[1]

def test_map():
    for pair in zip(analogue_map(math.cos,[1,2,3,4]),map(math.cos,[1,2,3,4])):        assert pair[0] == pair[1]
    for pair in zip(analogue_map(math.cos,[-1,0,0,0]),map(math.cos,[-1,0,0,0])):
        assert pair[0] == pair[1]


def test_enumerate(data):
    for pair in zip(analogue_enumerate(data,1),enumerate(data,1)):
        assert pair[0] == pair[1]
    for pair in zip(analogue_enumerate(data,0),enumerate(data,0)):
        assert pair[0] == pair[1]





