import sys
from pyfiglet import Figlet

figlet = Figlet()

first = sys.argv[0]

if len(sys.argv) == 3:
    if sys.argv[1] != "-f":
        sys.exit(1) #Code failure
        
    if sys.argv[2] in figlet.getFonts():
        userInput = input("Input: ")
        figlet.renderText(userInput)
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(userInput))
    else:
        sys.exit(1) #Code failure
else:
    sys.exit(1) #Code failure


