expression = input("Expression: ")

x, y, z = expression.split(" ")
#Définir x et z:
x1= float(x)
z1= float(z)

# Faire chaque situation
if y == "+":
    result = x1 + z1

if y == "-":
    result = x1 - z1

if y == "*":
    result = x1 * z1

if y == "/":
    result = x1 / z1

print(round(result, 1))
