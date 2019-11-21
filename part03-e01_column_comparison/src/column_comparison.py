#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    b = []
    second = a[:,1]#second column to compare
    secondLast = a[:,-2]#seond last
    b = second > secondLast
    #print(a[b])
    return np.array(a[b]])
    
def main():
    #a=np.random.randint(0, 10, (5,6))
    a = [[8,9,3,8,8,],[0,5,3,9,9],[5,7,6,0,4],[7,8,1,6,2],[2,1,3,5,8]]
    a = np.array(a)
    
    print(column_comparison(a))
    pass

if __name__ == "__main__":
    main()
