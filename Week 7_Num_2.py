import tabulate
import sys
import csv

#oublie pas de faire le changement a chaque fois 
if len(sys.argv) == 2:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            print (tabulate.tabulate(reader,headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File not found")

