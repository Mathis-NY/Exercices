from datetime import date
import sys
import inflect

p = inflect.engine()



def main():
    try:
        year, month, day = input("Date of Birth: ").split("-")
    except ValueError:
        sys.exit("Invalid Date")

    print(minute_user(year, month, day))





def minute_user(year, month, day):
    try:
        naissance = date(int(year), int(month), int(day))
    except ValueError:
        return "Invalid Date"

    today = date.today()
    diff = today - naissance
    minutes = int(diff.total_seconds()/60)
    #pour print en minute il font utiliser un variable, plus simple et utiliser number_to_word

    message = p.number_to_words (minutes, andword=" ") + " minutes" #andword pour enlever le and
    return message.capitalize()




if __name__ == "__main__":
    main()
