import numpy as np
from PIL import Image,ImageDraw

Max_Iterations = 50

w = 2000
h = 2000

lr = .5
ll = -2
lu = 1.25
ld = -1.25

def shade(c:complex):
    '''returns the number of iterations needed to diverge'''
    z = 0+0j
    for i in range(Max_Iterations):
        
        z=z*z + c

        if abs(z) > 2:
            return int((i*255)/Max_Iterations)
        
    return int((i*255)/Max_Iterations)

def canvas(width,height):

    im = np.zeros((width,height))

    dx = (lr-ll)/width
    dy = (lu-ld)/height

    for x in np.arange(ll,lr,dx):

        for y in np.arange(ld,lu,dy):

            a = int((x-ll)/dx)
            b = int((y-ld)/dy)
            im[a,b] = shade(complex(x,y))

    return im


def image(canvas:np.array):
    
    width = canvas.shape[0]
    height = canvas.shape[1]

    img = Image.new('RGB',(width,height),(0,0,0,0))
    draw = ImageDraw.Draw(img)

    for i in range(width):
        for j in range(height):

            a = int(canvas[i,j])
            
            color = (0,a,a)
            draw.point((i,j),fill=(color))

    img.save('mandelbrot.jpg',quality=100)
                



if __name__ == '__main__':

    image(canvas(w,h))