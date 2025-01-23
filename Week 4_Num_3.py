liste = { }


while True:
    try:
        item = input().lower()

        if item in liste:
            liste[item] +=1

        else:
            liste[item] = 1


    except EOFError:

        for key in sorted(liste.keys()):
            print(liste[key], key.upper())
        break
