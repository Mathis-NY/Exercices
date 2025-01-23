bank = input("Greeting: ").lower().strip()

if bank.startswith("hello"):
    print("$0")

elif bank.startswith("h"):
    print("$20")

else:
    print("$100")
