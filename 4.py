#!/usr/bin/bash
# Problem - http://www.pythonchallenge.com/pc/def/linkedlist.php

# Thought Process - Follow the chain,
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
# and the next nothing is 44827
# pass the number as next argument to ?nothing=44827
# Yes. Divide by two and keep going.
# for this divide the number by 2 i.e. 16044/2 = 8022 and then pass the argument

# Solution - http://www.pythonchallenge.com/pc/def/peak.html

import urllib.request

link = "12345"
while(True):
	get = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+link).read()

	string = get.decode("utf-8")
	print(string)
	splitStr = string.split()
	if splitStr[0] == "Yes.":
		link = str(int(link)/2)
	else:
		link = splitStr[-1]
	print(link)


# Solution - peak.html
