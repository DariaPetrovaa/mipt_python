import pytest

@pytest.fixture()
def some_data_1():
    names = ["Alex", "Bob", "Alice"]
    age = [25, 17]
    return names,age

@pytest.fixture()
def some_data_2():
    names = ["Alex"]
    age = [25, 17]
    return names,age

@pytest.fixture()
def some_data_3():
    names = ["Alex", "Bob", "Alice"]
    age = [25, 17, 0, 16, 14]
    return names,age

@pytest.fixture()
def data():
    names = ["Alex", "Bob", "Alice"]
    return names

@pytest.fixture()
def lists1():
    lists = [
        [5, 4],
        [7, 8, 9],
        [5, 7, 8, 9, 10]
    ]
    return lists

@pytest.fixture()
def lists2():
    lists = [
        [100, 9],
        [9, 0, 0],
        [5, 7.9, 8, -1, 11]
    ]
    return lists

@pytest.fixture()
def lists3():
    lists = [
        [3, 4],
        [7, 9.8],
        [7.9, 6]
    ]
    return lists



    

