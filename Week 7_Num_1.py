import sys

def main():
    evenement()

    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
    except FileNotFoundError:
        sys.exit ("File does not exist")

    nombre_line = 0
    for line in lines:
        if loop(line) == False:
            nombre_line += 1
    print (nombre_line)




def evenement():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")


def loop(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False



if __name__ == "__main__":
    main()
