import main


def test_add():
    a = 1
    b = 2
    assert 3 == main.add(a, b)


def test_getPanda():
    expected = "panda"
    actual = main.getPanda().at[0, 0]
    assert expected == actual
