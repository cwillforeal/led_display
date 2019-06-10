"""Two functions to check if an image is downloadable and to resize it"""

from PIL import Image
import requests
from io import BytesIO
import math
import csv
import cProfile
import re

def is_downloadable(url):
    """Checks if the url contains a downloadable resource"""
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True, url

#print(is_downloadable('http://www.wwurugby.org/wp-content/uploads/2012/10/122-1024x768.jpg'))
#print(is_downloadable('http://google.com/favicon.ico'))
#print(is_downloadable('https://is1-ssl.mzstatic.com/image/thumb/Purple19/v4/3e/c8/9c/3ec89c0f-8406-155a-0322-cd53c81253ea/pr_source.png/246x0w.jpg'))


def compress_img(img_url):
    """Shrinks an image fetched from URL to a 15x15"""
    url = img_url 
    response = requests.get(url) #uses requests package to fetch the image
    img = Image.open(BytesIO(response.content)) #uses BytesIO to get basic info from image like file type, mode, size
    print(img)

    smallimg = img.resize((15,15)) #uses PIL package to resize the height and width of the image. returns a new Image object, does not modify o.g. image
    print(smallimg) #prints to prove the size has change
    smallimg.save('smallimg.png') #saves new image to the same directory as the python script


def thumbnail_img():
    """Shrinks an image but keeps aspect ratio"""
    image_to_thumbnail = Image.open('sunset.png')
    image_to_thumbnail.thumbnail((90, 90))
    image_to_thumbnail.save('sunset_thumbnail.png')
    
def pixel_edit():
    """test to see if changing pixel color in predtermined location is possible"""
    img = Image.open('sunset.png')
    numxpixels = 2000
    numypixels = 10
    for i in range(numxpixels):
        for j in range(numypixels):
            changepixelcolortogreen = img.putpixel([i,j],(0, 255, 94)) #accesses pixels (numxpixels and numypixels) and changes the RGB value to 0, 255, 94. 
    img.save('changedpixel.png')

def get_info():
    """return basic information about the image"""
    img = Image.open('sunset.png')
    return img.format, img.mode, img.size, img.palette

def grouppixels_getavgcolor():
    """splits image into chunks and loops through pixels in the chunks to get their values and then finds the average RGB value for each chunk"""
    img = Image.open('sunrise.jpg')
    imagesize = img.size
    chunks = []
    r = []
    g = []
    b = []
    chunksize = 15
    xlen = math.floor(imagesize[0] / chunksize)
    print("xlen = {}".format(xlen))
    ylen = math.floor(imagesize[1] / chunksize)
    print("ylen = {}".format(ylen))

    countchunks = 0

    for x in range(0, chunksize): #this first run gives us x values
        for y in range(0, chunksize): #this run gives us y values
            chunks.append([])
            r.append([])
            g.append([])
            b.append([])
            for x2 in range(0, xlen):
                for y2 in range(0, ylen):
                    #chunks[countchunks].append((x*xlen+x2,y*ylen+y2))
                    chunks[countchunks].append(img.getpixel((x*xlen+x2,y*ylen+y2)))
                    r[countchunks].append(img.getpixel((x*xlen+x2,y*ylen+y2))[0])
                    g[countchunks].append(img.getpixel((x*xlen+x2,y*ylen+y2))[1])
                    b[countchunks].append(img.getpixel((x*xlen+x2,y*ylen+y2))[2])
            countchunks += 1

    avgr = []
    avgg = []
    avgb = []

    for i in r:
        avgr.append(int(sum(i)/len(i)))
    for i in g:
        avgg.append(int(sum(i)/len(i)))
    for i in b:
        avgb.append(int(sum(i)/len(i)))
   
    return avgr, avgg, avgb


import itertools

def grouppixels_getavgcolor2():
    """#2 tries to append averages to the end of the image which doesn't get picked up
    because there is a remainder on the x axis because 400/15 has a remainder"""
    img = Image.open('sunrise.jpg')
    imagesize = img.size
    r = []
    g = []
    b = []
    chunksize = 15
    xlen = math.floor(imagesize[0] / chunksize)
    print("xlen = {}".format(xlen))
    ylen = math.floor(imagesize[1] / chunksize)
    print("ylen = {}".format(ylen))
    countchunks = 0

    for x in range(0, chunksize): #this first run gives us x values
        for y in range(0, chunksize): #this run gives us y values
            r.append([])
            g.append([])
            b.append([])
            for x2 in range(0, xlen):
                for y2 in range(0, ylen):
                    r[countchunks].append(img.getpixel((x*xlen+x2,y*ylen+y2))[0])
                    g[countchunks].append(img.getpixel((x*xlen+x2,y*ylen+y2))[1])
                    b[countchunks].append(img.getpixel((x*xlen+x2,y*ylen+y2))[2])
            countchunks += 1

    avgr = []
    avgg = []
    avgb = []

    for i in r:
        avgr.append(int(sum(i)/len(i)))
    for i in g:
        avgg.append(int(sum(i)/len(i)))
    for i in b:
        avgb.append(int(sum(i)/len(i)))

    
    def grouper(n, iterable, fillvalue=None):
        args = [iter(iterable)] * n
        return itertools.zip_longest(fillvalue=fillvalue, *args)
    rlist = list(grouper(1, avgr, avgr[224]))
    print(len(avgr))
    print(len(rlist))
   
    return rlist, avgg, avgb
    

def changecolor(rgb):
    img = Image.open('sunrise.jpg')
    imagesize = img.size
    chunksize = 15
    xlen = math.floor(imagesize[0] / chunksize)
    ylen = math.floor(imagesize[1] / chunksize)
    countchunks2 = 0
    for x in range(0, chunksize):
        for y in range(0, chunksize):
            for x2 in range(0, xlen):
                for y2 in range(0, ylen):
                    #print(x*xlen+x2,y*ylen+y2)
                    newsunsetthumbnail = img.putpixel([x*xlen+x2,y*ylen+y2], ((rgb[0][countchunks2], rgb[1][countchunks2], rgb[2][countchunks2])))
            countchunks2 +=1
               
    img.save('newsunrise.jpg')
    print('Image size is {}'.format(imagesize))
    print('X remainder is {} and Y remainder is {}'.format(imagesize[0] % 15, imagesize[1] % 15))
    print('done')
                   
    
    
if __name__ == "__main__":
    #get_info()
    #thumbnail_img()
    avg_rgb = grouppixels_getavgcolor2()
    print(avg_rgb)
    changecolor(avg_rgb)
    #cProfile.run('re.compile("foo|bar")')
    #compress_img('https://en.es-static.us/upl/2018/06/sun-pillar-6-25-2018-Peter-Gipson-sq.jpg')
    #pixel_edit()


"""
If the image isn't divisible by 15, then we can use this code to fill in the remaining pixels with some value.
testlist = [4,6,7,4,2,4,6]
testavg = int(sum(testlist)/len(testlist))

import itertools
imglist = list(range(0, 2000))
def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=fillvalue, *args)

fifteenpixeltest = list(grouper(15, imglist, testavg))
print(fifteenpixeltest)
print((fifteenpixeltest[133]))"""

