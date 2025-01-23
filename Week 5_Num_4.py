import random

while True:
    try:
        userInput = int(input("Level: "))
        if userInput < 1:
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

number = random.randint(1, 10)

while True:
    try:
        userInputGuess = int(input("Guess: "))
        if userInputGuess > number:
            print("Too large!")
        elif userInputGuess < number:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

