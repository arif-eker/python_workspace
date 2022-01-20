#
#
# topic numbers = [1, 2, 3, 4, 5]
# CTRL + F and enter --topic number-- for jump topic to topic
# for example "--5--"

# datetime = time + dae modules


import datetime as dt

#########################################################################################################################################################
# Topic: --1--

print(dt.MINYEAR)  #
print(dt.MAXYEAR)  # 9999

print(dt.datetime.today())  # 2022-01-20 15:57:15.090181
my_date = dt.datetime.today()

print(my_date.microsecond)  # 341011
print(my_date.second)  # 1

print(my_date.minute)  # 59
print(my_date.hour)  # 15

print(my_date.day)  # 20
print(my_date.month)  # 1

print(my_date.year)  # 2022
print(my_date.time())  # 15:59:01.341011

print(my_date.date())  # 2022-01-20
print(my_date.ctime())  # Thu Jan 20 15:59:01 2022 --> str

print(my_date.astimezone())  # 2022-01-20 15:59:01.341011+03:00

# return day of the week, where Monday == 1 and Sunday == 7
print(my_date.isoweekday())  # 4

# return day of the week, where Monday == 0 and Sunday == 6
print(my_date.weekday())  # 3

# return a 3-tuple (year, week, weekday)  week : what week of the year for example 43. week
print(my_date.isocalendar())  # (2022, 3, 4)

dt.datetime.now()  # --> similar to datetime.today()

#########################################################################################################################################################
# Topic: --2--

new_date = dt.datetime(2018, 12, 25, 15, 10, 0)
print(new_date.isocalendar())  # (2018, 52, 2)

print(new_date)  # 2018-12-25 15:10:00
print(f"year: {new_date.year} month: {new_date.month} day: {new_date.day}")  # year: 2018 month: 12 day: 25

#########################################################################################################################################################
# Topic: --3--

print(my_date.strftime("%y"))  # 22
print(my_date.strftime("%Y"))  # 2022

print(my_date.strftime("%d"))  # 20  # day
print(my_date.strftime("%D"))  # 01/20/22

print(my_date.strftime("%a"))  # Thu
print(my_date.strftime("%A"))  # Thursday

print(my_date.strftime("%b"))  # Jan
print(my_date.strftime("%B"))  # January

print(my_date.strftime("%c"))  # Thu Jan 20 15:59:01 2022
print(my_date.strftime("%C"))  # 20

print(my_date.strftime("%m"))  # 01  # month
print(my_date.strftime("%M"))  # 59  # minute

print(my_date.strftime("%x"))  # 01/02/22
print(my_date.strftime("%X"))  # 15:59:01

print(my_date.strftime("%W"))  # 03  --> week of the year :Monday is the first week day
print(my_date.strftime("%U"))  # 03 --> week of the year :Monday is the first week day

print(my_date.strftime("%j"))  # 020 --> day of the year

print(my_date.strftime("%H"))  # 15  --> hour (24 hours)
print(my_date.strftime("%I"))  # 03  --> hour (12 hours)

print(my_date.strftime("%S"))  # second

print(my_date.strftime("%f"))  # microsecond
print(my_date.strftime("%p"))  # PM   --> time period AM/PM

#########################################################################################################################################################
# Topic: --4--

# create date from string values

my_str = "01/02/1998"  # --> day/month/year
str_date = dt.datetime.strptime(my_str, "%d/%m/%Y")
print(str_date)  # 1998-02-01 00:00:00

my_str = "01/02/98"
str_date = dt.datetime.strptime(my_str, "%d/%m/%y")
print(str_date)  # 1998-02-01 00:00:00

my_str = "Thu Jan 20 15:59:01 2022"
str_date = dt.datetime.strptime(my_str, "%a %b %d %X %Y")
print(str_date)  # 2022-01-20 15:59:01

#########################################################################################################################################################
# before
my_str = "Salı Ocak 20 15:59:01 2022"
str_date = dt.datetime.strptime(my_str,
                                "%A %B %d %X %Y")  # ValueError: time data 'Salı Ocak 20 15:59:01 2022' does not match format '%a %b %d %X %Y'

# after
# for turkish string
import locale

locale.setlocale(locale.LC_ALL, "en")

my_str = "Salı Ocak 20 15:59:01 2022"
str_date = dt.datetime.strptime(my_str, "%A %B %d %X %Y")
print(str_date)  # 2022-01-20 15:59:01

#########################################################################################################################################################
# Topic: --5--

# datetime object - datetime object --> timedelta object
# datetime object - timedelta object --> datetime object
# timedelta object - timedelta object --> timedelta object

time1 = dt.datetime(2018, 11, 25, 15, 10, 0)
time2 = dt.datetime(2018, 12, 25, 12, 25, 0)

result = time2 - time1

print(type(result))  # <class 'datetime.timedelta'>
print(result)  # 29 days, 21:15:00

print(result.microseconds)  # 0
print(result.seconds)  # 76500
print(result.days)  # 29
print(result.total_seconds())  # 2582100.0

my_delta = dt.timedelta(days=15)
result_date = time1 - my_delta

print(type(result_date))  # <class 'datetime.datetime'>
print(result_date)  # 2018-11-10 15:10:00

#
# datetime object + timedelta object --> datetime object
# timedelta object + timedelta object --> timedelta object

new_date = dt.datetime(2021, 1, 13)
time1 = dt.timedelta(days=3)
mydate = new_date + time1
print(mydate)  # 2021-01-16 00:00:00

res_time = dt.timedelta(days=3) + dt.timedelta(days=4)
print(res_time)  # 7 days, 0:00:00
