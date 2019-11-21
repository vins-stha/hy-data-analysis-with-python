#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    fig, ax = plt.subplots(1,2)

    
    first = a[:,0]
    second = a[:,1]
    third = a[:,2]
    fourth = a[:,3]#.astype(float)
    
    
    #plt.subplot(1, 2, 1)
    ax[0].plot(first,second,"*")

    # plt.subplot(1,2,2)
    ax[1].scatter(first,second,c=third,s=fourth)

    plt.show()


def main():
    n= 4
    a = np.random.randint(0,10,(n,4))
    subfigures(a)
    #pass"

if __name__ == "__main__":
    main()
