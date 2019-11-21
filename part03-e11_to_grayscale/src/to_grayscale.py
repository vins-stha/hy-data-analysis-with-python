#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def to_grayscale(a):
    color =a[:,:,:3]
    
    plt.subplot(221)
    plt.title("To grayscale")
    gray = np.dot(color , [0.2126 , 0.7152, 0.0722]) #np.dot(color , [0.2126 , 0.7152, 0.0722]) )
    
    return gray
   
 
def to_red(a):

    rows,columnss=a.shape[:2]
  
    for i in range((rows)):
        for j in range((columnss)):
            a[i,j,0] = a[i,j,0] * 1
            a[i,j,1] = a[i,j,1]*0
            a[i,j,2] = a[i,j,2]*0
 
 
    return a

def to_green(a):
    rows,columnss=a.shape[:2]

    for i in range(rows):
        for j in range(columnss):
            a[i,j,0] = a[i,j,0] * 0
            a[i,j,1] = a[i,j,1] * 1
            a[i,j,2] = a[i,j,2] * 0
          
    return a

def to_blue(a):
    rows,columnss=a.shape[:2]

    for i in range(rows):
        for j in range(columnss):
            a[i,j,0] = a[i,j,0] * 0
            a[i,j,1] = a[i,j,1] * 0
            a[i,j,2] = a[i,j,2] * 1
          
  
    return a



def main():
    fig, ax = plt.subplots(2,2)
    #try:
    a = plt.imread("src/painting.png")
    b = plt.imread("src/image.jpg")
    a = b.copy()
    ax[0,0].plot()
    gray = to_grayscale(a)
    plt.imshow(gray, cmap=plt.get_cmap(name="gray"))

    plt.subplot(222)
    plt.title("to Red")
    red = to_red(a)
    plt.imshow(red)

    plt.subplot(223)
    plt.title("to Green")
    green = to_green(a)
    plt.imshow(green)
    
    plt.subplot(224)
    plt.title("to Blue")
    blue = to_blue(a)
    plt.imshow(blue)

   
    plt.show()
    

if __name__ == "__main__":
    main()
