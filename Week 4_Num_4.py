months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input ("Date: ")
    try:
        month, day, year= date.split("/")

        if (int (month) >= 1 and int(month) <=12) and (int(day) >= 1 and int (day) <= 31):
            break

    except:
        try:
            m1, d1, year = date.split(" ")
# faire le truc de la looop pour stoper
            for i in range(len(months)):
                if m1 == months[i]:
                    month = i + 1

            day = d1.replace(",", " ")# enlever le jour ici
            # copy paste the top one car loop again

            if (int (month) >= 1 and int(month) <=12) and (int(day) >= 1 and int (day) <= 31):
                break


        except:
            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")

