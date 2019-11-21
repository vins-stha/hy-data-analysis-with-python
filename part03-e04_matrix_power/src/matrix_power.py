#!/usr/bin/env python3
import numpy as np 
from functools import reduce

def matrix_power(a, n):
#    m = np.ndim(a)
    result =[]

    print(" peek in here ", [d[:] for d in a])
    if n>0:

        generator_expression = ([d[:] for d in a] for i in range(n)) #iterator for reduce function d gets the array a[] and iterates for n times
        result = reduce(lambda a,b: [#lambda function >> multiply matrix a , b where b=a (for this set)
                [a[0][0]*b[0][0]+a[0][1]*b[1][0], a[0][0]*b[0][1]+a[0][1]*b[1][1]],
                [a[1][0]*b[0][0]+a[1][1]*b[1][0], a[1][0]*b[0][1]+a[1][1]*b[1][1]]
            ], generator_expression)#generator_Expression>> multiply the result of lambda a,b with generatior expression
        print(type(result))
        #print("result ",r)
    if n<0:
        n= -1*n
        print("your n = ", n)
        generator_expression = ([d[:] for d in a] for i in range(n)) #iterator for reduce function
        result = reduce(lambda a,b: [
                [a[0][0]*b[0][0]+a[0][1]*b[1][0], a[0][0]*b[0][1]+a[0][1]*b[1][1]],
                [a[1][0]*b[0][0]+a[1][1]*b[1][0], a[1][0]*b[0][1]+a[1][1]*b[1][1]]
            ], generator_expression)
       # print("result ",r)
        result = np.linalg.inv(result)
        #print(r)
    else: 
         if n == 0:
             result = np.eye(2)
        #print(np.eye(m, dtype=int))
             print(np.eye(2))#default provided!!!
 
    return result


def main():
    a = np.array([[1,2], [3,4]])
    n= [-3,0,3,1]
    n =3
    (matrix_power(a,n)) 

    
    
    

if __name__ == "__main__":
    main()
