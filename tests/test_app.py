from myapp.app import add, substruct

def test_add():
    assert add(2, 3) == 5

def test_substruct():
    assert substruct(5, 3) == 2
