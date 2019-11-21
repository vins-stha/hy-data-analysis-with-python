#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    a = np.full((n,n),1)
    
    col = np.arange(n).reshape(1,n)
    row = np.arange(n).reshape(n,1)

    colA = a*col
    result = colA * row
    print(a,col,row,result)
    return np.array(result)

def main():
    print(multiplication_table(6))

if __name__ == "__main__":
    main()
