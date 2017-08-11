#!/usr/bin/bash

# Problem - http://www.pythonchallenge.com/pc/def/peak.html
# Thought Process -
# peak hell sounds familiar ? "peak hell" - "pickle"
# Source file gives <peakhell src="banner.p" />
# copy the html text in a file named banner.p
# .p is a pickled file in python
# opening banner.p gives a serialized object

# Solution - http://www.pythonchallenge.com/pc/def/channel.html

import pickle

# deserialize the object file
fileObject = open("banner.p", 'r')
b = pickle.load(fileObject)

# a multidimesional list of tuples gives an ascii art with channel as solution
sol = ""
for i in range(len(b)):
  for j in range(len(b[i])):
    item = b[i][j]
    k = 0
    while(k < item[1]):
      sol += item[0]
      k += 1
  sol += "\n"

print(sol)

# Solution - channel
