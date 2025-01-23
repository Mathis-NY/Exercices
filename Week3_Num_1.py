camelCase = input("camelCase: ")

camelCase = camelCase[0].lower() + camelCase[1:]

for m in camelCase:
    if m.isupper():
        camelCase = camelCase.replace(m, f"_{m.lower()}")

print("snake_case:",camelCase)
