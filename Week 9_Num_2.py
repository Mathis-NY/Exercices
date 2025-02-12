class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.capacity2 = capacity
        self.size2 = 0

    def __str__(self):
        return ("🍪")* self.size

    def deposit(self, n):
        if n > self.capacity or n + self.size > self.capacity:
            raise ValueError
        self.size2 += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self.size2 -= n

    @property
    def capacity(self):
        return self.capacity2

    @property
    def size(self):
        return self.size2

def main():
    jar = Jar(12)
    jar.deposit(10)
    jar.withdraw(1)
    print (jar.capacity)
    print (jar.size)



if __name__ == "__main__":
    main()
