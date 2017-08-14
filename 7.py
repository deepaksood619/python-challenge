#!/usr/bin/python
# Problem - http://www.pythonchallenge.com/pc/def/oxygen.html

# Thought process - 
# 1. There is a grey scale gradient in the middle of the image
# 2. Run a loop over length and read the middle pixel value in the image
# 3. 7 represent that every 7th value must be read as values are repeating itself
# 4. convert the values to its ascii value, we get
# 5. smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]pe_
# 6. igonore the last 3 characters as they are gitter
# 7. take the dictionary and again convert it in ascii values
# 8. We get integrity

# Solution - http://www.pythonchallenge.com/pc/def/integrity.html

from PIL import Image

png = Image.open("oxygen.png")
pix = png.load()

x = 0
y = png.size[1] / 2
ans = ""
while(x < png.size[0]):
	ans += str(chr(pix[x,y][0]))
	x += 7

print(ans)
# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]pe_

foo = [105, 110, 116, 101, 103, 114, 105, 116, 121]

bar = ""
for i in foo:
  bar += str(chr(i))

print(bar)
# integrity