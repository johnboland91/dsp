# Hint:  use Google to find python function
import datetime as dt
###a) 
date_start = '01-02-2013'.split("-")
year1 = int(date_start[2])
month1 = int(date_start[0])
day1 = int(date_start[1])
date1 = dt.date(year1,month1,day1)

date_stop = '07-28-2015'.split("-")
year2 = int(date_stop[2])
month2 = int(date_stop[0])
day2 = int(date_stop[1])
date2 = dt.date(year2,month2,day2)

print(date2 - date1)

####b)  
import datetime as dt

date_start = '12312013'
year1 = int(date_start[4:])
month1 = int(date_start[0:2])
day1 = int(date_start[2:4])
date1 = dt.date(year1,month1,day1)

date_stop = '05282015'  
year2 = int(date_stop[4:])
month2 = int(date_stop[0:2])
day2 = int(date_stop[2:4])
date2 = dt.date(year2,month2,day2)

print(date2 - date1)

####c)  
import calendar
import datetime as dt

months = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

date_start = '15-Jan-1994'.split("-")
year1 = int(date_start[2])
month1 = months[date_start[1]]
day1 = int(date_start[0])
date1 = dt.date(year1,month1,day1)

date_stop = '14-Jul-2015'.split("-")
year2 = int(date_stop[2])
month2 = months[date_stop[1]]
day2 = int(date_stop[0])
date2 = dt.date(year2,month2,day2)
date2 = dt.date(year2,month2,day2)

print(date2 - date1)
 
