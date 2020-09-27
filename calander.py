import datetime
#import time-->not required
import calendar
"""mon tue wed thurs fri sat sun
    0    1   2   3    4    5   6"""
##print(calendar.weekheader(2))#Mo Tu We Th Fr Sa Su
##print(calendar.firstweekday())#0-->monday 
##print(calendar.month(2020,9))
##"""   September 2020
##Mo Tu We Th Fr Sa Su
##    1  2  3  4  5  6
## 7  8  9 10 11 12 13
##14 15 16 17 18 19 20
##21 22 23 24 25 26 27
##28 29 30"""
##print(calendar.calendar(2020))#complete 2020 calendar prints
##print(calendar.weekday(2020,9,12))#5-->saturday
##print(calendar.isleap(2020))#True
##
##print(datetime.date.today())#2020-09-12
currenttime=(datetime.datetime.now())
print(currenttime)#2020-09-12 08:42:36.141746
print(currenttime.month)#9
##print(currenttime.day)#12
##print(currenttime.hour)#8
##print(currenttime.minute)#42
##
###to know how many days in between
##given_date=(datetime.date(2019,9,21))
##return_date=datetime.date.today()#2020-09-12
##no_of_days=(return_date - given_date).days
##print(no_of_days)#357

print(calendar.day_name[calendar.weekday(2020,9,15)].upper())#TUESDAY
