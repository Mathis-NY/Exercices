# The number of 'perpetrators armed with guns' was not mentioned in the instructions, but it appeared in the example, so I included it in the program.

import csv

dict = {}
with open ('lawEnforcement.csv') as infile:
    reader = csv.reader(infile)
    header = next(reader)

    for rec in reader:
        date = rec[0]
        weapon = rec[1]
        age = int(rec[2])
        gender = rec[3]
        state = rec[4]


        incident = [date, age, weapon, gender]

        if state in dict :
            dict[state].append(incident)

        else:
            dict[state] = [incident]

state = input("Enter state abbreviation: ")

print()
print("date".ljust(12), "age".ljust(6), "weapon".ljust(15), "gender")
print()

for incident in dict[state]:
    print(incident[0].ljust(12), str(incident[1]).ljust(6), incident[2].ljust(15), incident[3])


#Print the average age of the perpetrators involved in the incidents associate with the state#
#Print the average age of the perpetrators involved in the incidents associate with the state#
#Print the average age of the perpetrators involved in the incidents associate with the state#
print()
average_age = 0

for incident in dict[state]:
    average_age = average_age + incident[1]

mean_age = round(average_age / len(dict[state]))

print("Average age of perpetrators in", state + ":", mean_age)


# Print the number of perpetrators armed with guns in the state
# Print the number of perpetrators armed with guns in the state
# Print the number of perpetrators armed with guns in the state

gun_count = 0

for incident in dict[state]:
    if incident[2] == "gun":
        gun_count = gun_count + 1

print("Number of perpetrators armed with guns in", state + ":", gun_count)




# Print the number of perpetrators in the state who were female
# Print the number of perpetrators in the state who were female
# Print the number of perpetrators in the state who were female

female_count = 0

for incident in dict[state]:
    if incident[3] == "F":
        female_count = female_count + 1

print("Number of female perpetrators in", state + ":", female_count)

# Print the number of perpetrators in the state who were male
# Print the number of perpetrators in the state who were male
# Print the number of perpetrators in the state who were male

male_count = 0

for incident in dict[state]:
    if incident[3] == "M":
        male_count = male_count + 1

print("Number of male perpetrators in", state + ":", male_count)
print()
