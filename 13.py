#!/usr/bin/python

# Problem - http://www.pythonchallenge.com/pc/return/disproportional.html

# Thought process -
# there is a link in 5 number
# using that we get a xml @ http://www.pythonchallenge.com/pc/phonebook.php
# it is giving error so something must be there
# also <remote /> tag is used in the page source.
# so we get to xmlrpc using remote and xml document trees as breadcrumbs
# using that we get phone as one of the methods
# using methodHelp and methodSignature we get that it takes a string and returns a string
# Since we have to call evil and in last level we got that bert is evil! go back
# so we have to call bert
# use python3.x because xmlrpc is part of that and not python2.x

# Solution - http://www.pythonchallenge.com/pc/return/italy.html

import xmlrpc.client

r = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(r.phone("Bert"))

# 555-ITALY
# now trying all the combinations of 555-italy in the url we get the solution
# after seeing the answer we got to know that 555 is fake number in US.