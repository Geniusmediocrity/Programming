import calendar


year = int(input())
clndr = calendar.calendar(year, 3)
cal = clndr.getfirstweekday()
print(cal)