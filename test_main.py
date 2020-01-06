import main


def test_add():
    a = 1
    b = 2
    assert 3 == main.add(a, b)


def test_sub():
    a = 1
    b = 2
    assert 1 == main.sub(a, b)
