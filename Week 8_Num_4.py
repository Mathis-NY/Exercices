# um.py

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    mots_count = re.findall(r"\b(um)\b", s, re.IGNORECASE)
    return len(mots_count)


...


if __name__ == "__main__":
    main()




#pytest test_um.py


from um import count

def main():
    test_1()
    test_2()
    test_3()


def test_1():
    assert count ("um") == 1

def test_2():
    assert count ("um, um. yummy") == 2

def test_3():
    assert count ("Um, salut mon amis") == 1
    assert count ("comment ca va? ") == 0


if __name__ == "__main__":
    main()


