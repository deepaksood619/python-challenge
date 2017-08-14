#!/usr/bin/python

# problem - http://www.pythonchallenge.com/pc/return/evil.html

# thought process -
# 1. title - dealing evil
# 2. evil1.jpg
# 3. trying evil2.jpg
# 4. we get gfx instead of jpg
# 5. try evil2.gfx we got the gfx
# 6. trying evil3 and else doesn't give anything
# 7. now reading gfx file and getting content

# solution - http://www.pythonchallenge.com/pc/return/disproportional.html

data = open("evil2.gfx", "rb").read()
for i in range(5):
    open('%d.jpg' % i ,'wb').write(data[i::5])

# dis pro port ional ity(cut)
# disproportional