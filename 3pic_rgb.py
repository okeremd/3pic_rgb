from cv2 import imread, imwrite, resize, bitwise_not
from numpy import zeros
from os.path import isfile, isdir
from os import mkdir
from datetime import datetime

def rgb(r,g,b, file, day):
    size = r.shape
    arr = zeros(size)

    arr[:,:,0] = b[:,:,0]
    arr[:,:,1] = g[:,:,1]
    arr[:,:,2] = r[:,:,2]

    middir = 'output/{}_{}_{}_{}_{}_{}'.format(day.year, day.month, day.day, day.hour, day.minute, day.microsecond)
    outputdir = 'output/{}_{}_{}_{}_{}_{}/{}'.format(day.year, day.month, day.day, day.hour, day.minute, day.microsecond, file)
    
    if(not isdir('output')):
        mkdir('output')
    if(not isdir(middir)):
        mkdir(middir)
    if(not isdir(outputdir)):
        mkdir(outputdir)
    imwrite('{}/rgb.jpg'.format(outputdir), arr)

    arr[:,:,0] = g[:,:,0]
    arr[:,:,1] = b[:,:,1]
    arr[:,:,2] = r[:,:,2]
    
    imwrite('{}/rbg.jpg'.format(outputdir), arr)

    arr[:,:,0] = r[:,:,0]
    arr[:,:,1] = g[:,:,1]
    arr[:,:,2] = b[:,:,2]
    
    imwrite('{}/bgr.jpg'.format(outputdir), arr)

    arr[:,:,0] = g[:,:,0]
    arr[:,:,1] = r[:,:,1]
    arr[:,:,2] = b[:,:,2]
    
    imwrite('{}/brg.jpg'.format(outputdir), arr)

    arr[:,:,0] = b[:,:,0]
    arr[:,:,1] = r[:,:,1]
    arr[:,:,2] = g[:,:,2]
    
    imwrite('{}/grb.jpg'.format(outputdir), arr)

    arr[:,:,0] = r[:,:,0]
    arr[:,:,1] = b[:,:,1]
    arr[:,:,2] = g[:,:,2]
    
    imwrite('{}/g(e)b(e)r(zaa).jpg'.format(outputdir), arr)


def main():
    if(isfile('r.jpg')):
        r = imread('r.jpg')
    elif(isfile('r.png')):
        r = imread('r.png')
    elif(isfile('r.jpeg')):
        r = imread('r.jpeg')
    else:
        return -1

    if(isfile('g.jpg')):
        g = imread('g.jpg')
    elif(isfile('g.png')):
        g = imread('g.png')
    elif(isfile('g.jpeg')):
        g = imread('g.jpeg')
    else:
        return -1

    if(isfile('b.jpg')):
        b = imread('b.jpg')
    elif(isfile('b.png')):
        b = imread('b.png')
    elif(isfile('b.jpeg')):
        b = imread('b.jpeg')
    else:
        return -1

    size = r.shape
    print(size)
    g = resize(g, tuple([size[1], size[0]]))
    b = resize(b, tuple([size[1], size[0]]))

    nr = bitwise_not(r)
    ng = bitwise_not(g)
    nb = bitwise_not(b)

    day = datetime.today()
    rgb(r, g, b, 'rgb', day)
    rgb(r, g, nb, 'rg-b', day)
    rgb(r, ng, b, 'r-bg', day)
    rgb(nr, g, b, '-rgb', day)
    rgb(r, ng, nb, 'r-g-b', day)
    rgb(nr, g, nb, '-rg-b', day)
    rgb(nr, ng, b, '-r-gb', day)
    rgb(nr, ng, nb, '-r-g-b', day)


        
main()
