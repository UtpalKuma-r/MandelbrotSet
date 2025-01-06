#Imports
import PIL.Image as image
import numpy
import cmath
import math
import colorsys

def bounded(z, c, n=1000)->tuple:
    '''Function tho check if the given complex number lies in maldelbrot set.
        It takes 3 inputs
        z : initial complex number
        c : complex number
        n : (Optional, Default=1000) Number of iteration 
        return: RGB values (R, G, B)'''
    if n>0:
        z1 = z*z + c
        if abs(z1) > 2:
            return colour(n - math.log(math.log2(abs(z1))))
            # return(0, 255, 255)
        return bounded(z1, c, n-1)
    # return colour(n)
    return (0, 0, 0)

def colour(n):
    color = 255 * numpy.array(colorsys.hsv_to_rgb(n / 255.0, 0.5, 0.5))
    return tuple(color.astype(int))

def main():

    size = (100000, 100000) #Size of the image
    im = image.new(mode="RGB", size=size) # creating a new image object
    arr = im.load()
    itter = 100 #How many times the recursion should run
    partPixelSize = 10000 #size of each part

    parts = int(size[0]/partPixelSize) #no. of parts the image will be generated in

    # for i in range(parts):
    #     for j in range(parts):
    i = 0

    for pixel_x in range(partPixelSize):
        for pixel_y in range(partPixelSize):
            Rpixel_x = (partPixelSize*i)+pixel_x
            Rpixel_y = (partPixelSize*i)+pixel_y
            z_realPart = (Rpixel_x-(2*size[0]/3))/(size[0]/3)
            z_imagenaryPart = (Rpixel_y-(2*size[0]/3))/(size[0]/3)
            z = complex(z_realPart, z_imagenaryPart)
            x = bounded(0, z, itter)
            arr[Rpixel_x, Rpixel_y] = x
    i += 1

    for pixel_x in range(partPixelSize):
        for pixel_y in range(partPixelSize):
            Rpixel_x = (partPixelSize*i)+pixel_x
            Rpixel_y = (partPixelSize*i)+pixel_y
            z_realPart = (Rpixel_x-(2*size[0]/3))/(size[0]/3)
            z_imagenaryPart = (Rpixel_y-(2*size[0]/3))/(size[0]/3)
            z = complex(z_realPart, z_imagenaryPart)
            x = bounded(0, z, itter)
            arr[Rpixel_x, Rpixel_y] = x
    i += 1

    for pixel_x in range(partPixelSize):
        for pixel_y in range(partPixelSize):
            Rpixel_x = (partPixelSize*i)+pixel_x
            Rpixel_y = (partPixelSize*i)+pixel_y
            z_realPart = (Rpixel_x-(2*size[0]/3))/(size[0]/3)
            z_imagenaryPart = (Rpixel_y-(2*size[0]/3))/(size[0]/3)
            z = complex(z_realPart, z_imagenaryPart)
            x = bounded(0, z, itter)
            arr[Rpixel_x, Rpixel_y] = x
    i += 1

    for pixel_x in range(partPixelSize):
        for pixel_y in range(partPixelSize):
            Rpixel_x = (partPixelSize*i)+pixel_x
            Rpixel_y = (partPixelSize*i)+pixel_y
            z_realPart = (Rpixel_x-(2*size[0]/3))/(size[0]/3)
            z_imagenaryPart = (Rpixel_y-(2*size[0]/3))/(size[0]/3)
            z = complex(z_realPart, z_imagenaryPart)
            x = bounded(0, z, itter)
            arr[Rpixel_x, Rpixel_y] = x
    i += 1

    for pixel_x in range(partPixelSize):
        for pixel_y in range(partPixelSize):
            Rpixel_x = (partPixelSize*i)+pixel_x
            Rpixel_y = (partPixelSize*i)+pixel_y
            z_realPart = (Rpixel_x-(2*size[0]/3))/(size[0]/3)
            z_imagenaryPart = (Rpixel_y-(2*size[0]/3))/(size[0]/3)
            z = complex(z_realPart, z_imagenaryPart)
            x = bounded(0, z, itter)
            arr[Rpixel_x, Rpixel_y] = x
    i += 1

    for pixel_x in range(partPixelSize):
        for pixel_y in range(partPixelSize):
            Rpixel_x = (partPixelSize*i)+pixel_x
            Rpixel_y = (partPixelSize*i)+pixel_y
            z_realPart = (Rpixel_x-(2*size[0]/3))/(size[0]/3)
            z_imagenaryPart = (Rpixel_y-(2*size[0]/3))/(size[0]/3)
            z = complex(z_realPart, z_imagenaryPart)
            x = bounded(0, z, itter)
            arr[Rpixel_x, Rpixel_y] = x
    i += 1

    for pixel_x in range(partPixelSize):
        for pixel_y in range(partPixelSize):
            Rpixel_x = (partPixelSize*i)+pixel_x
            Rpixel_y = (partPixelSize*i)+pixel_y
            z_realPart = (Rpixel_x-(2*size[0]/3))/(size[0]/3)
            z_imagenaryPart = (Rpixel_y-(2*size[0]/3))/(size[0]/3)
            z = complex(z_realPart, z_imagenaryPart)
            x = bounded(0, z, itter)
            arr[Rpixel_x, Rpixel_y] = x
    i += 1

    for pixel_x in range(partPixelSize):
        for pixel_y in range(partPixelSize):
            Rpixel_x = (partPixelSize*i)+pixel_x
            Rpixel_y = (partPixelSize*i)+pixel_y
            z_realPart = (Rpixel_x-(2*size[0]/3))/(size[0]/3)
            z_imagenaryPart = (Rpixel_y-(2*size[0]/3))/(size[0]/3)
            z = complex(z_realPart, z_imagenaryPart)
            x = bounded(0, z, itter)
            arr[Rpixel_x, Rpixel_y] = x
    i += 1

    for pixel_x in range(partPixelSize):
        for pixel_y in range(partPixelSize):
            Rpixel_x = (partPixelSize*i)+pixel_x
            Rpixel_y = (partPixelSize*i)+pixel_y
            z_realPart = (Rpixel_x-(2*size[0]/3))/(size[0]/3)
            z_imagenaryPart = (Rpixel_y-(2*size[0]/3))/(size[0]/3)
            z = complex(z_realPart, z_imagenaryPart)
            x = bounded(0, z, itter)
            arr[Rpixel_x, Rpixel_y] = x
    i += 1

    for pixel_x in range(partPixelSize):
        for pixel_y in range(partPixelSize):
            Rpixel_x = (partPixelSize*i)+pixel_x
            Rpixel_y = (partPixelSize*i)+pixel_y
            z_realPart = (Rpixel_x-(2*size[0]/3))/(size[0]/3)
            z_imagenaryPart = (Rpixel_y-(2*size[0]/3))/(size[0]/3)
            z = complex(z_realPart, z_imagenaryPart)
            x = bounded(0, z, itter)
            arr[Rpixel_x, Rpixel_y] = x
    i += 1


    im.show()
    im.save("MandelbrotSet.png")
    im.save("MandelbrotSet.tiff")

if __name__ == "__main__":
    main()
