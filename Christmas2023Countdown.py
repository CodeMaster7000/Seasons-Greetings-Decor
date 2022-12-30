import datetime
dt = datetime.datetime
now = dt.now()
timeLeft = dt(year = 2023, month = 12, day = 25) - dt(year=now.year, month=now.month, day=now.day)
print "Days left until Christmas:"
print timeLeft.days
