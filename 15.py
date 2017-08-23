#!/usr/bin/python
# Problem - http://www.pythonchallenge.com/pc/return/uzi.html

# Thought Process -
# Title - whom?
# Source - 
#  1. <!-- he ain't the youngest, he is the second -->
#  2. <!-- todo: buy flowers for tomorrow -->
# Image - A calendar with 26 as circled

# image got a hole with 1xx6 and 1 january as thrusday

# Solution - http://www.pythonchallenge.com/pc/return/mozart.html

# thrusday - 3

import datetime

start = 1006;

while start <= 1996:
    if datetime.date(start, 1, 1).weekday() == 3:
        # year must be a leap year as feb 29 is given in calendar
        if start%4 == 0:
            print(start)
    start += 10

# 1176, 1356, 1576, 1756, 1976
# so get the second yongest
# 26-jan-1756
# buy flowers for tomorrow-
# 27-jan-1756
# whom?
# Birthday of Wolfgang Amadeus Mozart

# Solution - mozart