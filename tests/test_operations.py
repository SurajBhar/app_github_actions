from src.math_operations import add, sub

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(5,3) == 8

def test_sub():
    assert sub(3,2) == 1
    assert sub(5,4) == 1
    assert sub(1,1) == 0