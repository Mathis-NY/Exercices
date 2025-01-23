while True:
    x = input("Fraction: ")
    try:
        numérateur, dénominateur = x.split ("/")

        numérateur= int(numérateur)
        dénominateur= int(dénominateur)

        y= numérateur/dénominateur

        mul = int(y*100)

        if mul <= 1:
            print("E")
            break
        if mul >=99:
            print ("F")
            break
        else:
            print (f"{mul}%")
            break

    except (ValueError, ZeroDivisionError):
        pass
