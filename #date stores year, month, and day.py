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

######################################################################### NEW SECTOR BELOW


# import the datetime and timedelta modules
from datetime import datetime, timedelta


# When you ask a user for a date tell them the desired date format
birthday = input('When is your birthday (dd/mm/yyyy)? ')


# When you convert the string containing the date into a date object
# you must specify the expected date format
# if the date is not in the expected format Python will raise an exception
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')


print ('Birthday: ' + str(birthday_date))


# Because we converted the string into a date object
# We can use date and time functions such as timedelta with the object
one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print('Day before birthday: ' + str(birthday_eve))
