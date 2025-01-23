
result = 50

while result > 0:
    print ("Amount Due:", result)
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:
          result = result - coin

if result <= 0:
        print ("Change Owed:", - result)

else:
      print("Error")




