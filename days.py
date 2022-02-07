from datetime import date

x1 = int(input("Enter year1: "))
y1 = int(input("Enter month1: "))
z1 = int(input("Enter day1: "))
print('-'*40)
x2 = int(input("Enter year2: "))
y2 = int(input("Enter month2: "))
z2 = int(input("Enter day2: "))

f_date = date(x1, y1, z1)
l_date = date(x2, y2, z2)

delta = l_date - f_date
print('-'*40)
print(f'Number of days is {delta.days}')