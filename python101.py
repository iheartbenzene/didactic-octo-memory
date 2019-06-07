from datetime import datetime, date

today_mark_i = datetime.today()
print(today_mark_i)

print(type(today_mark_i))

date_of_today = date.today()
print(date_of_today)
print(date_of_today.year)
print(date_of_today.month)
print(date_of_today.day)

christmas = date(2019, 12, 25)
print(christmas)

if christmas is not date_of_today:
    print('There are ' + str((christmas - date_of_today).days) + ' days remaining until Christmas')
elif christmas == date_of_today:
    print('Yay, it\'s Christmas!')
else:
    print('According to that guy, this should be an error. But I couldn\'t think of one so...yeah.')