from plates import is_valid

def main():
    test_valid1()
    test_valid2()
    test_valid3()
    test_valid4()

def test_valid1():
    assert is_valid("c") == False
    assert is_valid("bonjour mon ami") == False
    assert is_valid("ps90") == True


def test_valid2():
    assert is_valid("23") == False
    assert is_valid("ca") == True

def test_valid3():
    assert is_valid("ps,';23") == False
    assert is_valid("ps23") == True

def test_valid4():
    assert is_valid("ps09") == False
    assert is_valid("ps90") == True
    assert is_valid("ps90a") == False

