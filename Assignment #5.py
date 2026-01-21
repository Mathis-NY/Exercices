salaries = []
names = []

name = input ('Enter an employee name: ')

while name != 'exit':
    names.append(name)
    salary = int(input('Enter a salary: '))
    salaries.append(salary)
    name = input('Enter an employee name: ')


print()

LargeSalary = 0
print ('Names' .ljust (10), 'Salaries' .rjust(8), 'Weekly'.rjust(10), 'Weekly Net' .rjust(12))

for i in range(0, len(names)):
    weeklyPay = salaries[i] // 52
    weeklyPay = round(weeklyPay)

    if weeklyPay >= 2000:
        tax = 0.20
    elif weeklyPay >= 1500:
        tax = 0.15
    else:
        tax = 0.10

    weeklyNetPay = weeklyPay - (weeklyPay * tax)
    weeklyNetPay = round(weeklyNetPay)
    if salaries[i] > salaries[LargeSalary]:
        LargeSalary = i

    print (names[i].ljust(10), str(salaries[i]).rjust(8), str(weeklyPay).rjust(10), str(weeklyNetPay).rjust (12))

print()


#4 #4 #4 #4

print()

print()

print(names[LargeSalary], 'has the largest salary with the values listed below.')
print('Salary:'.ljust(12), str(salaries[LargeSalary]).rjust(10))

weeklyPay = round(salaries[LargeSalary] // 52)

if weeklyPay >= 2000:
    tax = 0.20
elif weeklyPay >= 1500:
    tax = 0.15
else:
    tax = 0.10

weeklyNetPay = round(weeklyPay - (weeklyPay * tax))
weeklyNetPay = round(weeklyNetPay)

print('Weekly:'.ljust(12), str(weeklyPay).rjust(10))
print('Weekly Net:'.ljust(12), str(weeklyNetPay).rjust(10))

print()


print()






#5 #5 #5 #5

print()

LowerSalary = 0
for i in range(len(salaries)):
    if salaries[i] < salaries[LowerSalary]:
        LowerSalary = i

print(names[LowerSalary], 'has the lowest salary with the values listed below.')
print('Salary:'.ljust(12), str(salaries[LowerSalary]).rjust(10))

weeklyPay = round(salaries[LowerSalary] // 52)

if weeklyPay >= 2000:
    tax = 0.20
elif weeklyPay >= 1500:
    tax = 0.15
else:
    tax = 0.10

weeklyNetPay = round(weeklyPay - (weeklyPay * tax))
weeklyNetPay = round(weeklyNetPay)

print('Weekly:'.ljust(12), str(weeklyPay).rjust(10))
print('Weekly Net:'.ljust(12), str(weeklyNetPay).rjust(10))

print()




#6 #6 #6 #6

print()

print()

weeklyPays = []
weeklyNetPays = []

for salary in salaries:
    weeklyPay = salaries[i] // 52
    weeklyPay = round(weeklyPay)

    if weeklyPay >= 2000:
        tax = 0.20
    elif weeklyPay >= 1500:
        tax = 0.15
    else:
        tax = 0.10

    weeklyNetPay = round(weeklyPay - (weeklyPay * tax))
    weeklyNetPay = round(weeklyNetPay)

    weeklyPays.append(weeklyPay)
    weeklyNetPays.append(weeklyNetPay)

averageSalary = round(sum(salaries) / len(salaries))
averageWeekly = round(sum(weeklyPays) / len(weeklyPays))
averageWeeklyNet = round(sum(weeklyNetPays) / len(weeklyNetPays))

print('Average Salary:'.ljust(22), str(averageSalary).rjust(10))
print('Average Weekly:'.ljust(22), str(averageWeekly).rjust(10))
print('Average Weekly Net:'.ljust(22), str(averageWeeklyNet).rjust(10))

print()

#7 #7 #7 #7
print()
print('People with salaries that are less than the average salary are listed below.')
print('Names'.ljust(10), 'Salaries'.rjust(8), 'Weekly'.rjust(10), 'Weekly Net'.rjust(12))

for i in range(len(salaries)):
    if salaries[i] < averageSalary:
        weeklyPay = round(salaries[i] // 52)

        if weeklyPay >= 2000:
            tax = 0.20
        elif weeklyPay >= 1500:
            tax = 0.15
        else:
            tax = 0.10

        weeklyNetPay = round(weeklyPay - (weeklyPay * tax))

        print(names[i].ljust(10),
              str(salaries[i]).rjust(8),
              str(weeklyPay).rjust(10),
              str(weeklyNetPay).rjust(12))
print()



