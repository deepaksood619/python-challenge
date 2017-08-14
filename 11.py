#!/usr/bin/python

# Problem - http://www.pythonchallenge.com/pc/return/5808.html

# Thought process -
# 1. by seeing the image itself we can say that the image is combination of two or more images
# 2. Its a classical problem of steganography
# 3. title says "odd even" means odd row consists of one image and even the other.
# 4. but image pixels are collection of two coordinate points
# 5. add both the coordinates, if the sum is divisible by 2 add pixel to even and if not add pixel to odd

# Solution - http://www.pythonchallenge.com/pc/return/evil.html

from PIL import Image

im = Image.open("cave.jpg")

pix = im.load()
newImEven = Image.new("RGB", (im.size[0]/2, im.size[1]/2))
even = newImEven.load()
newImOdd = Image.new("RGB", (im.size[0]/2, im.size[1]/2))
odd = newImOdd.load()

for x in range(0, im.size[0]):
	for y in range(0, im.size[1]):
		sum = x + y
		if(sum % 2 == 0):
			even[x/2, y/2] = pix[x, y]
		else:
			odd[x/2, y/2] = pix[x, y]

newImEven.save("even.jpg", "JPEG")
newImOdd.save("odd.jpg", "JPEG")
Image.open("even.jpg").show()
Image.open("odd.jpg").show()

# evil in even.jpg