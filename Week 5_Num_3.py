tab = []
text = "and"
try:
    while True:
        line = input("Name: ")
        x = line.replace("Name:","")
        tab.append(x)
        # ici faut process the line
except EOFError:
    if len(tab) == 1:
        p = f"Adieu, adieu, to, {tab[0]}"
    else:
        p = f"Adieu, adieu, to {', '.join(tab[:-1])}, {text} {tab[-1]}"
    print("\n", p)

