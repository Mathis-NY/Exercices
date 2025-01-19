def main():
    a = int(input("Chiffre 1: "))
    b = int(input("Chiffre 1: "))
    result = sum2numbers(a, b)
    #j'ai regarde sur google car je n'arrivais pas a faire disparaitre ce putain de none
    # ps: pas de chat
    if result is not None:
        print(result)

def sum2numbers(a, b):
    if a >= 0 and b >= 0:
        return (a + b)
    else:
        print ("Veuillez retourner un chiffre positif")
        return None

main()
