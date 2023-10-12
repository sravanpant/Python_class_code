from datetime import date, time, datetime

date_input = date(1988, 10, 31)
date_today = date.today()
print(date_input)
print(date_today)
if date_input == date_today:
    print("date is equal")
elif date_input > date_today:
    print("date is ahead")
else:
    print("date is behind")
