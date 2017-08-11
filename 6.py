#!/usr/bin/python
# Problem - http://www.pythonchallenge.com/pc/def/channel.html

# Thought Process - zip is written, download channel.zip
# also there is a zip in the image
# http://www.pythonchallenge.com/pc/def/channel.zip
# extract zip
# zip contains files with name to next file

# the last file says collect comments, there is properties associated with each file, we hbave to collect it

# Solution - http://www.pythonchallenge.com/pc/def/oxygen.html

import zipfile

f = zipfile.ZipFile("channel.zip")

foo = "90052"

comments = []

while(True):
  bar = f.read(foo + ".txt", 'r').decode("utf-8")
  comments.append(f.getinfo(foo + ".txt").comment.decode("utf-8"))
  print(bar)
  etc = bar.split()[-1]
  if etc != "comments.":
    foo = bar.split()[-1]
    print(foo)
  else:
    break

print("".join(comments))

# solution - hockey
# going to hockey it says - "it's in the air. look at the letters."# looking at the letters of ASCII arts we get oxygen
