#!/usr/bin/python

# Problem - http://www.pythonchallenge.com/pc/return/bull.html

# Thought process -
# 1. the source has a polyfill shape, clicking on which we get a sequence.txt
# 2. a = [1, 11, 21, 1211, 111221
# 3. the question says len(a[30]) = ?
# 4. Googling sequence gives Look-and-say-sequence
# 5. now we have to find the length of a[30]

# Solution - http://www.pythonchallenge.com/pc/return/5808.html

a = "1"
print("0 - "+a)
run = 0
while(run < 30):
	run += 1
	b = ""
	j = 0
	while(j < len(a)):
		count = 1
		while(j+1 < len(a) and a[j] == a[j+1]):
			count += 1
			j += 1
		b += str(count) + a[j]
		j += 1
	print(str(run) + " - " + b)
	print("length - " + str(len(b)))
	a = b

# Solution - 5808