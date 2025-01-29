# import re
# import sys


# def main():
#     print(convert(input("Hours: ")))


# def convert(s):
#     temps = re.search (r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s, re.IGNORECASE)
#     if temps:
#         if temps.group(2):
#             if int(temps.group(2)) >= 60:
#                 raise ValueError
#         if temps.group(5):
#             if int(temps.group(5)) >= 60:
#                 raise ValueError


#             il s'agit de la partie 1 ici

#         heure1 = int(temps.group(1))
#         if temps.group(3) == "PM" and heure1 != 12:
#             heure1 += 12
#         elif temps.group(3) == "AM" & heure1 == 12:
#             heure1 -= 12
#         if temps.group(2) == None:
#             temps1 = f"{heure1:02}:00"
#         else:
#             temps1 = f"{heure1:02}:{temps.group(2)}

#             il s'agit de la partie 2 ici

#         heure2 = int(temps.group(4))
#         if temps.group(6) == "PM" and heure2 != 12:
#             heure2 += 12
#         elif temps.group(5) == "AM" and heure2 == 12:
#             heure2 -= 12
#         if temps.group(5) == None:
#             temps2 = f"{heure2:02}:00"
#         else:
#             temps2 = f"{heure2:02}:{temps.group(5)}


#         temps = f"{temps1} to {temps2}"
#         return temps


# essaie de regarder avec regex101, plus rapide & simple
#     else:
#         raise ValueError




# if __name__ == "__main__":
#     main()



import re

# ----------- MAIN FUNCTION ------------ #

def main():
    print(convert(input("Hours: ")))


# ----------- CONVERT HOURS ------------ #


def convert_hours(h, am_pm):
    # return (h+12) if it is "PM" and but not 12 PM:
    if am_pm == "PM" and int(h) != 12:
        return (int(h) + 12)

    # return 0 if it is 12 AM:
    elif am_pm == "AM" and int(h) == 12:
        return 0

    # otherwise if it is not PM, or not 12 AM or PM, return 'h' as it is:
    return h


# ----------- CONVERT FUNCTION ------------ #


def convert(s):
    # find matches to the pattern, "?P<h1>" represents the capture group which is quantity of hour of first time:
    matches = re.search(r"^(?P<h1>\d{1,2})(:| )(?P<m1>\d{2})? ?(?P<am_pm1>\w{2}) to (?P<h2>\d{1,2})(:| )(?P<m2>\d{2})? ?(?P<am_pm2>\w{2})", s)

    # detect early and raise ValueError if there is no matches:
    if matches is None:
        raise ValueError

    h1 = matches.group("h1")
    h2 = matches.group("h2")
    m1 = matches.group("m1")
    m2 = matches.group("m2")
    am_pm1 = matches.group("am_pm1")
    am_pm2 = matches.group("am_pm2")

    try:
        # check if both hours are valid, else raise Value Error:
        if 1 <= int(h1) <= 12 and 1 <= int(h2) <= 12:

            # check if AM or PM are present, else raise Value Error:
            if am_pm1 and am_pm2 in ["AM", "PM"]:

                # if both minute values exist, check that they are in range (between 0 & 59) if they both exist (e.g. 9:"30" AM, 12:"45" PM)
                if m1 != None and m2 != None and 0 <= int(m1) <= 59 and 0 <= int(m2) <= 59:

                    # pass h1 and h2 to the function created before:
                    h1 = convert_hours(h1, am_pm1)
                    h2 = convert_hours(h2, am_pm2)

                    return f"{int(h1):02}:{m1:02} to {int(h2):02}:{m2:02}"

                # if m1 doesn't exist and m2 does, check if m2 is in range (e.g. 9 AM to 5:30 PM):
                elif m1 == None and m2 != None and 0 <= int(m2) <= 59:
                    h1 = convert_hours(h1, am_pm1)
                    h2 = convert_hours(h2, am_pm2)
                    return f"{int(h1):02}:00 to {int(h2):02}:{m2:02}"

                # if m1 exists and m2 doesn't, check if m1 is in range (e.g. 9:30 AM to 5 PM):
                elif m1 != None and m2 == None and 0 <= int(m1) <= 59:
                    h1 = convert_hours(h1, am_pm1)
                    h2 = convert_hours(h2, am_pm2)
                    return f"{int(h1):02}:{m1:02} to {int(h2):02}:00"

                # if m1 and m2 don't exist (e.g. 9 AM to 5 PM):
                elif m1 == None and m2 == None:
                    h1 = convert_hours(h1, am_pm1)
                    h2 = convert_hours(h2, am_pm2)
                    return f"{int(h1):02}:00 to {int(h2):02}:00"

                else:
                    raise ValueError

            else:
                raise ValueError

        else:
            raise ValueError

    except:
        raise ValueError


# ----------- CALL MAIN ------------ #

if __name__ == "__main__":
    main()

# ----------- END ------------ #
