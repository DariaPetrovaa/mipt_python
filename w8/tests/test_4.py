import pytest
from tasks.task_4 import get_cartesian_product

@pytest.mark.parametrize('test_input,expected_result',[(get_cartesian_product([1, 2], [3, 4]),[(1, 3), (1, 4), (2, 3), (2, 4)]), (get_cartesian_product([0, -1], ['a', 'c']),[(0, 'a'), (0, 'c'), (-1, 'a'), (-1, 'c')]),(get_cartesian_product(['x', 2], [3, 'v']),[('x', 3), ('x', 'v'), (2, 3), (2, 'v')]),(get_cartesian_product([0, 0], ['dog', 'cat']),[(0, 'dog'), (0, 'cat'), (0, 'dog'), (0, 'cat')])])
def test_product(test_input,expected_result):
    assert test_input == expected_result

