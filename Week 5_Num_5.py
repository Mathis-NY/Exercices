# # import random


# # def main():

# #     nombre_questions = 10
# #     score = 0


# #     level = get_level()

# #     for _ in range(nombre_questions):
# #         if question(level):
# #             score += 1

# #     print(f"{score}/{nombre_questions}")


# # def get_level():
# #     while True:
# #         try:
# #             level = int(input("Level: "))
# #             if 1 <= level <= 3:
# #                 return level
# #             else:
# #                 print("Invalid level. Please enter a number between 1 and 3.")
# #         except ValueError:
# #             print("Invalid input. Please enter a positive integer.")

# # def generate_integer(level):
# #     if level == 1:
# #         return random.randint(0, 9)
# #     elif level == 2:
# #         return random.randint(10, 99)
# #     elif level == 3:
# #         return random.randint(100, 999)


# # def question(level):
# #     num1 = generate_integer(level)
# #     num2 = generate_integer(level)



# #     operations = ["+", "-", "*"]
# #     operation = random.choice(operations)




# #     if operation == "+":
# #         correct_answer = num1 + num2
# #     elif operation == "-":
# #         correct_answer = num1 - num2
# #     elif operation == "*":
# #         correct_answer = num1 * num2

# #     while True:
# #         try:
# #             user_answer = int(input(f"What is {num1} {operation} {num2}? "))
# #             if user_answer == correct_answer:
# #                 print("Correct!")
# #                 return True
# #             else:
# #                 print("Incorrect. The correct answer was:", correct_answer)
# #                 return False
# #         except ValueError:
# #             print("Invalid input. Please enter an integer.")




# # if __name__ == "__main__":
# #     main()


# import random


# def main():

#     nombre_questions = 10
#     score = 0


#     level = get_level()

#     for _ in range(nombre_questions):
#         if question(level):
#             score += 1

#     print(f"{score}/{nombre_questions}")



# def get_level():
#     while True:
#         try:
#             level = int(input("Level: "))
#             if 1 <= level <= 3:
#                 return level
#             else:
#                 print("Invalid level. Please enter a number between 1 and 3.")
#         except ValueError:
#             print("Invalid input. Please enter a positive integer.")

# def generate_integer(level):
#     if level == 1:
#         return random.randint(0, 9)
#     elif level == 2:
#         return random.randint(10, 99)
#     elif level == 3:
#         return random.randint(100, 999)


# def question(level):
#     num1 = generate_integer(level)
#     num2 = generate_integer(level)



#     operations = ["+", "-", "*"]
#     operation = random.choice(operations)




#     if operation == "+":
#         correct_answer = num1 + num2
#     elif operation == "-":
#         correct_answer = num1 - num2
#     elif operation == "*":
#         correct_answer = num1 * num2

#     while True:
#         try:
#             user_answer = int(input(f"What is {num1} {operation} {num2}? "))
#             if user_answer == correct_answer:
#                 print("Correct!")
#                 return True
#             else:
#                 print("Incorrect. The correct answer was:", correct_answer)
#                 return False
#         except ValueError:
#             print("Invalid input. Please enter an integer.")




# if __name__ == "__main__":
#     main()



import random


def main():
    level = get_level()
    total_questions = 10
    score = 0


    for _ in range(total_questions):
        if ask_question(level):
            score += 1

    
    print(f"Score: {score}/{total_questions}")


def get_level():
    """Prompt user for a valid level (1, 2, or 3)."""
    while True:
        try:
            level = int(input("Level (1, 2, or 3): "))
            if 1 <= level <= 3:
                return level
            else:
                print("Invalid level. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def generate_integer(level):
    """Generate a random integer based on the level."""
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


def ask_question(level):
    """Generate and ask a math problem, handling incorrect attempts."""
    num1 = generate_integer(level)
    num2 = generate_integer(level)
    correct_answer = num1 + num2

    attempts = 0
    while attempts < 3:
        try:
            user_answer = int(input(f"{num1} + {num2} = "))
            if user_answer == correct_answer:
                return True
            else:
                print("EEE")
                attempts += 1
        except ValueError:
            print("EEE")
            attempts += 1


    print(f"{num1} + {num2} = {correct_answer}")
    return False


if __name__ == "__main__":
    main()




