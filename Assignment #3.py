hours = int(input('Enter hours parked: '))

x = hours - 2
y = 5
a = 17
b = hours - 8



if hours <= 2 :
    price = 5

elif hours > 2 and hours <= 8 :
    price = (x * 2) + y

elif hours > 8 and hours <= 24 :
    price = (b * 1.5) + a

else :
    print ('Wrong number')
    exit()

if price > 25:
    price = 25


print ('Your parking fee for',hours, 'hours is', price, '$')
