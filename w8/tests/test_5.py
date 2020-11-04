import pytest
from tasks.task_5 import get_permutations

@pytest.mark.parametrize('test_input,expected_result',[(get_permutations('cat',2),["ac", "at", "ca", "ct", "ta", "tc"]), (get_permutations('123',3),['123', '132', '213', '231', '312', '321']),(get_permutations('physics', 0), ['']),(get_permutations('physics', 10), [])])
def test_product(test_input,expected_result):
    assert test_input == expected_result
