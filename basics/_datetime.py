import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A, %B %d, %Y"))

date = datetime.datetime(2018, 5, 18)
print(date)
print(date.strftime("%c"))

print(x.strftime("%c"))

t = datetime.time(14, 18, 11)
print(t)
print(t.strftime("%S"))

date_str = "2025-10-01"
print(datetime.datetime.strptime(date_str, "%Y-%m-%d"))

created_at = datetime.date(2019, 3, 28)
print(created_at)
print(created_at.year)
print(created_at.month)

attended_at = datetime.time(10, 33, 45)
print(attended_at)
print(attended_at.second)
print(attended_at.hour)

now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)

difference = now - date
print(difference.days)

feature = now + datetime.timedelta(days=10)

print(feature)
