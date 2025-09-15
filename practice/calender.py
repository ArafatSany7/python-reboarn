import calendar

year = int(input("Enter year : "))
month = int(input("Enter Month : "))

cal = calendar.month(year, month)
print(cal)
