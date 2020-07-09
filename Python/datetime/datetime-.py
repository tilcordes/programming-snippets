import datetime

# returns the date
tday = datetime.datetime.now()
print(tday)

# returns the date and the time
daytime = datetime.datetime.now()
print(daytime)

# creates a timedelta with 6 days, 1 hour and 5 seconds, which you can add to a date
tdelta = datetime.timedelta(days=6, hours=1, seconds=5)
print(daytime + tdelta)

# converts a datetime to a string in a specific format
dateformated = daytime.strftime('%B %d, %Y %H:%M')
print(dateformated)