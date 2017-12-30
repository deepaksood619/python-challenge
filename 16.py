#!/usr/bin/python
# Question - http://www.pythonchallenge.com/pc/return/mozart.html

# Title - let me get this straight

# Image - its a gif
# image consists of only one frame
# printing the pixel values give only one number 
# Image is a greyscale image since it has only one number for each pixel from 0 to 255

# we have pink pixel in the images and its said we have to get this straight
# so align all the pink pixel

# Solution - http://www.pythonchallenge.com/pc/return/romance.html

import numpy as np
from PIL import Image

image = Image.open("mozart.gif")
shifted = [bytes(np.roll(row, -row.tolist().index(195)).tolist()) for row in np.array(image)]
Image.frombytes(image.mode, image.size, b"".join(shifted)).show()

# romance
# romance.html