import pytest
from tasks.task_7 import get_combinations_with_r

@pytest.mark.parametrize('test_input,expected_result',[(get_combinations_with_r('cat',2),['aa', 'ac', 'at', 'cc', 'ct', 'tt']),(get_combinations_with_r('cat',3),['aaa', 'aac', 'aat', 'acc', 'act', 'att', 'ccc', 'cct', 'ctt', 'ttt']),(get_combinations_with_r('cat',0),['']),(get_combinations_with_r('1234',1),['1', '2', '3', '4']),(get_combinations_with_r('1',3),['111'])])
def test_combinations(test_input,expected_result):
    assert test_input == expected_result
