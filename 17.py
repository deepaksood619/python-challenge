#!/usr/bin/python

# Question - http://www.pythonchallenge.com/pc/return/romance.html

# Title - eat?
# image name is cookies
# small image that is embedded is from level 4
# level 4 was a redirecting question

# level 4 question - http://www.pythonchallenge.com/pc/def/linkedlist.php

from urllib.request import urlopen
from urllib.parse import unquote_plus, unquote_to_bytes
import re, bz2

num = '12345'
info = ''
while(True):
    h = urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='+num)
    raw = h.read().decode("utf-8")
    print(raw)
    cookie = h.getheader("Set-Cookie")
    info += re.search('info=(.*?);', cookie).group(1)
    match = re.search('the next busynothing is (\d+)', raw)
    if match == None: 
        break
    else:
        num = match.group(1)
res = unquote_to_bytes(info.replace("+", " "))
print(res)
print(bz2.decompress(res).decode())
# is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand