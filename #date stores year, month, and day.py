#date stores year, month, and day
#time stores hour, minute, and second
#datetime stores year, month, day, hour, minute, and second
#timedelta a duration of time between two dates, times, or datetimes
# strptime() converts sting to date/time

#To get current date and time we need to use the datetime library
from datetime import datetime, timedelta
# The now function returns current date and time
today = datetime.now()

print("Today is: " + str(today))
#You can use timedelta to add or remove days, or weeks to a date
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

one_week = timedelta(weeks=1)
last_week = today - one_week
print('Last week was: ' + str(last_week))

######################################################################### NEW SECTOR BELOW

#To get current date and time we need to use the datetime library
from datetime import datetime

# The now function returns current date and time
today = datetime.now()

# use day, month, year, hour, minute, second functions
# to display only part of the date
# All these functions return integers
# Convert them to strings before concatenating them to another string
print('Day: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))

print('Hour: ' + str(today.hour))
print('Minute: ' + str(today.minute))
print('Second: ' + str(today.second))

