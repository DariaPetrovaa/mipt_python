import pytest
from tasks.task_9 import maximize

def test_max(lists1,lists2,lists3):
    assert maximize(lists1,1000) == 206
    assert maximize(lists2,10) == 2    #(100**2+9**2+11**2)%10 or (9**2+11**2)%10
    assert maximize(lists3,18) == 16   #(4**2)%18



