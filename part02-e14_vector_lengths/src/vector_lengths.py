#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    
        
    sq_a = np.power(a,2)
    
    sq_a = np.array(sq_a)

    sum_a = np.sqrt(sq_a.sum(axis = 1))
    
   
   
    
       
    return sum_a
def main():
    a = [[1,2,3,4,5],[4,5,6,1,2],[7,8,9,1,1]]
    a = np.array(a)
    a=np.random.randint(-100, 100, (4,5))
    print(vector_lengths(a))
    pass

if __name__ == "__main__":
    main()
