#!/usr/bin/python

# Problem - http://www.pythonchallenge.com/pc/def/integrity.html

# Thought process -
# 1. In the source, we can see that there is a poly area defined on click of which a page is redirected
# 2. Clicking on the page or the poly shape in the image a page is opened asking for username and password
# 3. In source, there is un, pw that stands for username and password.
# 4. Its a bzip2 compressed string (Quick search for BZh in google gave the answer)
# 5. decompress the given strings
# 6. We get username: huge and password: file
# 7. we login via the username and password and that's the solution

# Solution - http://www.pythonchallenge.com/pc/return/good.html

import bz2

un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

print(bz2.decompress(un))
# huge

print(bz2.decompress(pw))
# file