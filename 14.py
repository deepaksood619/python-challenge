#!/usr/bin/python
# Problem - http://www.pythonchallenge.com/pc/return/italy.html

# Thought process -
# an image wire.png with 10000x1 size
# hint given in source 100x100
# create a image with 100x100 using 10000x1 pixels

# Solution - http://www.pythonchallenge.com/pc/return/uzi.html

from PIL import Image

png = Image.open("wire.png")
pix = png.load()

im = Image.new("RGB", (100, 100))
newpix = im.load()

count = 0

for i in range(0,100):
    for j in range(0,100):
        newpix[j, i] = pix[count, 0]
        count += 1

im.save("out.png", "PNG")

# we get bit written in the image
# we go to bit.html
# Output - you took the wrong curve.

# we have to go in spiral as spiral image is shown
# and the title says walk around
# we go 100 pixels to right, then 99 to bottom and 99 to left side
# then 98 to up

im = Image.open('wire.png')

delta = [(1,0),(0,1),(-1,0),(0,-1)]
out = Image.new('RGB', [100,100])
x,y,p = -1,0,0
d = 200 
while d/2>0:
    for v in delta:
        steps = d // 2
        for s in range(steps):
            x, y = x + v[0], y + v[1]
            out.putpixel((x, y),im.getpixel((p,0)))
            p += 1
        d -= 1
out.save('out1.png', 'PNG')

# offcourse its image of a cat
# cat.html (and its name is uzi. you'll hear from him later. )
# uzi.html