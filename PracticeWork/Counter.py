'''import collections

w = "Python Programing Language"

d = collections.Counter(w)
print(d)'''


from datetime import date,timedelta, datetime

today = date.today()
now= datetime.now()
# Adding 7 days
future_date = today + timedelta(days=7)
print("Date after 7 days:", future_date)
# Subtracting 3 days
past_date = today - timedelta(days=3)
print("Date 3 days ago:", past_date)
# Adding 2 hours
future_time = now + timedelta(hours=2)
print("Time after 2 hours:", future_time)