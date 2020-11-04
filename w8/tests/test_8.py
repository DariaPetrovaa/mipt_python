import pytest
from tasks.task_8 import compress_string

@pytest.mark.parametrize('test_input,expected_result',[(compress_string('1222311'),[(1, 1), (3, 2), (1, 3), (2, 1)]),(compress_string('1'),[(1,1)]),(compress_string(''),[])])
def test_combinations(test_input,expected_result):
    assert test_input == expected_result
