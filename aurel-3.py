
a = int(input("Chiffre 1: "))
b = int(input("Chiffre 2: "))

method = input("Tu veux quoi poto? Salade, tomate, oignons? : ")

if method == ('-'):
    result = (a - b)


elif method == ('+'):
    result = (a + b)

elif method == ('*'):
    result = (a * b)

elif method == ('/'):
    quotient = a / b
    remainder = a % b
    result = f"Quotient: {quotient:.3f}, Reste: {remainder}"


print (result)
