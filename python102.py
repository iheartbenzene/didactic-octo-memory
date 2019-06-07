from datetime import datetime, date, timedelta

t = timedelta(days = 4, hours = 10)

print(t.days)
# print(t.hours)
# timedelta doesn't actually have a thing for "hours"
print(t.seconds)
print(t.seconds / 60 / 60)
print(t.seconds / 3600)

eta = timedelta(hours = 6)

today = datetime.today()

print(eta)
print(today + eta)
print(today + t)
print(today - eta)
print(today - t)