year = int(input("Enter a year : "))
if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a lear year".format(year))
elif (year % 4 == 0) and (year % 100 != 0):
    print(f"{year} is a lear year".format(year))
else:
    print(f"{year} is a not lear year".format(year))
