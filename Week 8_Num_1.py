import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    valid = re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip)
    if valid:
        for i in range (1, 5):
            if int(valid.group(i)) > 255:
                return False
        return True
    else:
        return False


...


if __name__ == "__main__":
    main()



#test_numb3rs.py
#test_numb3rs.py
#test_numb3rs.py
#test_numb3rs.py

for numb3rs import validate

def main():
    def IP_test_ok()
    def IP_test_not_ok()



def IP_test_ok():
    assert validate ("123.123.123.123") == True
    assert validate ("65.46.3.237") == True

def IP_test_not_ok():
    assert validate ("6543.464.334.237") == False
    assert validate ("vamosss") == False

if __name__ == "__main__":
    main()
