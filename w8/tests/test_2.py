import pytest
from tasks.task_2 import my_fib

@pytest.mark.parametrize("test_input, expected_result",[
(my_fib(1),[1]),
(my_fib(2),[1,1]),
(my_fib(5),[1,1,2,3,5]),
(my_fib(9),[1,1,2,3,5,8,13,21,34]), 
(my_fib(13),[1,1,2,3,5,8,13,21,34,55,89,144,233]),
(my_fib(15),[1,1,2,3,5,8,13,21,34,55,89,144,233,377,610])])
def test_fib(test_input,expected_result):
    assert test_input == expected_result
    
