#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.xlabel("My x-axis")
    plt.ylabel("My y-axis")
    plt.title("Multiple graphs")
    
    #a = np.array([2,4,6,7],[4,3,5,1])
    #b = np.array([1,2,3,4],[4,2,3,1])
    plt.plot([2,4,6,7], [4,3,5,1])
    plt.plot([1,2,3,4], [4,2,3,1])
    
    plt.show()
    
    pass

if __name__ == "__main__":
    main()
