"""
Walk through 10 and Exercixe 1
"""

from datetime import datetime as dt
# Get the current time, returns a value like 2022-10-09 17:46:45.151666
# Python flags for time
"""
        %a	Weekday, short version	Wed	
        %A	Weekday, full version	Wednesday	
        %w	Weekday as a number 0-6, 0 is Sunday	3	
        %d	Day of month 01-31	31	
        %b	Month name, short version	Dec	
        %B	Month name, full version	December	
        %m	Month as a number 01-12	12	
        %y	Year, short version, without century	18	
        %Y	Year, full version	2018	
        %H	Hour 00-23	17	
        %I	Hour 00-12	05	
        %p	AM/PM	PM	
        %M	Minute 00-59	41	
        %S	Second 00-59	08	
        %f	Microsecond 000000-999999	548513	
        %z	UTC offset	+0100	
        %Z	Timezone	CST	
        %j	Day number of year 001-366	365	
        %U	Week number of year, Sunday as the first day of week, 00-53	52	
        %W	Week number of year, Monday as the first day of week, 00-53	52	
        %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
        %C	Century	20	
        %x	Local version of date	12/31/18	
        %X	Local version of time	17:41:00	
        %%	A % character	%	
        %G	ISO 8601 year	2018	
        %u	ISO 8601 weekday (1-7)	1	
        %V	ISO 8601 weeknumber (01-53)	01
"""


today = dt.now()
print(today)
# Get Unix time, returns a value like 1665566809.057217
unix_epoch_time = dt.timestamp(today)
print(unix_epoch_time)

# lets do exercise 1, not that pritty but it works. I could have tried building a list or something but time is against me.
my_day= today.strftime("%A")
my_day_num = today.strftime("%d")
my_month = today.strftime("%B")
my_time = today.strftime("%X")
my_time_year = today.strftime("%Y")
my_full_date = (f"It is {my_day} the {my_day_num}th of {my_month} and the time is {my_time} in the year {my_time_year}")

print (my_full_date)
