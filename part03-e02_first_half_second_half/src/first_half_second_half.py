#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    
    shape = np.shape(a)
    n,m = shape[0],shape[1]
    
    first_half = int(m/2)
    leftM = int(shape[1])-first_half
    
    first_half = a[:,:(first_half)]
    second_half = a[:,leftM:]
  #  print("*********\n\n",first_half, "****************\n\n",second_half,"**************\n\n")
    compare = np.sum(first_half,axis=1)>np.sum(second_half,axis=1)
   

    result = a[compare]

   # print(result)
    
    return np.array(result)

def main():
    n=3
    m=2
    a = np.random.randn(n, 2*m)
    a = np.array([[1, 3, 4, 2],[2, 2, 0, 2]])
    #print(a)
    print(first_half_second_half(a))
    
   # pass

if __name__ == "__main__":
    main()
