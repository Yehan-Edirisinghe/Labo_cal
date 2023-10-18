import random
from PIL import Image,ImageDraw
import numpy as np

width  = 1000
height = 1000

canvas = np.empty((width,height))

img = Image.new('RGB',(width,height),(0,0,0,0))
draw = ImageDraw.Draw(img)


for i in range(width):
    for j in range(height):
        a = int(random.random()*255)
        color = (a,a,a)
        draw.point((i,j),fill=(color))
img.save('random_image.jpg',quality=90)