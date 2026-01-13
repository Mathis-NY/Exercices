# twenty = 2000 pennies
# ten = 1000 pennies
# five = 500 pennies
# dollar = 100 pennies
# quarter = 25 pennies
# dime = 10 pennies
# nickel = 5 pennies
# penny = 1 penny




penny = int(input('Enter a value as a number of pennies: '))
print (penny, 'pennies is equal to:')


#twenty
twenty = penny // 2000
print (twenty, 'twenties')
x = penny % 2000


#ten
ten = x // 1000
print (ten, 'tens')
x1 = x % 1000



# #five
five = x1 // 500
print (five, 'fives')
x2 = x1 % 500

# #dollar
dollar = x2 // 100
print (dollar, 'dollars')
x3 = x2 % 100


# #quarter
quarter = x3 // 25
print (quarter, 'quarters')
x4 = x3 % 25


# #dime
dime = x4 // 10
print (dime, 'dimes')
x5 = x4 % 10


# #nickel
nickel = x5 // 5
print (nickel, 'nickels')
x6 = x5 % 5


# #penny
pen = x6 // 1
print (pen, 'pennies')
x7 = x6 % 1


