import datetime
import pytz

time_now = datetime.date.today()

print(time_now)
print(time_now.month)
print(time_now.weekday())
print(time_now.isoweekday())


# TIme dalta

td = datetime.timedelta(days=100)

nd = time_now + td

print(nd)

for t in pytz.all_timezones:
    print(t)
