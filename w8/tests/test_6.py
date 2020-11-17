import pytest
from tasks.task_6 import get_combinations

@pytest.mark.parametrize('test_input,expected_result',[(get_combinations('cat',2),["a", "c", "t", "ac", "at", "ct"]),(get_combinations('123',0),[]),(get_combinations('1',3),['1']),(get_combinations('cat',-1),[])])
def test_combinations(test_input,expected_result):
    assert test_input == expected_result
