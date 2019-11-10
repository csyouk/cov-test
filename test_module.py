from module import hello_world
from module import name


def test_hello_world():
    assert 'Hell world' == hello_world()


def test_name():
    assert 'youk' == name()


def test_name2():
    assert 'youk' == name()
