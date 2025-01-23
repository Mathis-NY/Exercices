def main():

    user_Input = input("Input: ")
    print(shorten(user_Input))


def shorten(user_Input):
    voyelles = ["a","e","i","o","u","A","E","U","I","O"]

    for i in voyelles:
        if i in user_Input:
            user_Input = user_Input.replace(i, "")

    return user_Input

if __name__ == "__main__":
    main()
