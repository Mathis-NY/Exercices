side = int(input('Enter a value for the sides: '))

print()

for i in range(side):
    for j in range (side):
        if i == 0 or i == side - 1 or j == 0 or j == side - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()


print()

for i in range(side):
    for j in range(side):
        if i == side - 1 or j == 0 or i == j:
            print('*', end=' ')
        else:
            print(' ', end=' ')

    print()
