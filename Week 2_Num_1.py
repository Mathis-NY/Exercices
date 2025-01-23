def main():
    user = input("What is the Answer to the Great Question of Life, The Universe, and Everything? ").strip()
    if (user == "42" or user == "forty-two" or user == "forty two" or user == "Forty Two" or user == "FoRty TwO"):
        print("Yes")
    else:
        print("No")


main()
