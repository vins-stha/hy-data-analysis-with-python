#!/usr/bin/env python3

import numpy as np
import math 
import matplotlib.pyplot as plt

def center(a):
    y,x = a.shape[:2]
    center_y,center_x = (x-1)/2, (y-1)/2
    return (center_x,center_y)   # note the order: (center_y, center_x)

def radial_distance(a):
    #b = a.copy()
    h,w = a.shape[0],a.shape[1]
    cY,cX = center(a)
    c = np.zeros((h,w))

    for i in range(c.shape[0]):
        for j in range(c.shape[1]):
            c[i,j] = math.sqrt((i-cY)**2 + (j-cX)**2)

    return c


def scale(a, tmin=0.0, tmax=1.0):
    
    b = a.copy()
    b = np.interp(b , (b.min(), b.max()), (tmin,tmax))
    #print(center(b))
   
    return b


def radial_mask(a):
    
    b = radial_distance(a)
    c = scale(b)
    mask1 = abs(c-1)
    mask = 1-c
    print("center of maske ",center(mask))
    return mask

def radial_fade(a):
    #if a.shape[0]
    try:
        mask = radial_mask(a)
        masked = scale(mask).reshape(mask.shape[0],mask.shape[1],1)
    
        result = a * masked
        print("a * masked",result)
    except: 
        Exception
    
    return result

def fadex(image):
    height, width = image.shape[:2]
    m=np.linspace(0,1, width)
    
    m = m.reshape(1,width,1)
    print(m.shape,m)
    result = image*m
    #for i in range()         # note that we rely on broadcasting here
    print ("IMAGE{}* mASK{}==RESULT{}".format(image,m,result))
    return result



def main():
    a = plt.imread("src/painting.png")
    fig, ax = plt.subplots(3,1)
    n=2
    #a=np.zeros((n,8,3))
    #print("a ==",a)
    x,y = center(a)

    radial_distance(a)    
    scale(a)

    modified=fadex(a)
    print(modified.shape)
    

    ax[0].imshow(a)
    ax[1].imshow(radial_mask(a))
    #ax[2].imshow(radial_fade(a))
    ax[2].imshow(modified)

    plt.show()



if __name__ == "__main__":
    main()
