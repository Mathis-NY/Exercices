
from bank import value

def main():
    test1()
    test2()
    test3()

def test1():
    assert value("hello")== 0
    assert value("HELLO")== 0
    assert value("HELLO")== 0

def test2():
    assert value('Hey')== 20
    assert value('hi')== 20
    assert value('HI')== 20


def test3():
    assert value('jdnfn')== 100
    assert value('yo')== 100

if __name__ == "__main__":
    main()
