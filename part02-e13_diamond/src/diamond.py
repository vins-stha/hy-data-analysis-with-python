#!/usr/bin/env python3
"""
[0 0 1           0 0]
[0 1 0           1 0]
[1 0 0           0 1]



[0 1 0           1 0]
[0 0 1           0 0]]

"""
import numpy as np

def diamond(n):
    if n >1:
        a = np.eye(n, dtype=int)
        A = a[::-1]#reverse the a 
    # print (A)

        #b = A[:,0:2]##concat first two columns to A ie 0-0 results 0-0-
        
        #c= np.concatenate((A,a))
        
        
        #c= np.delete(c,(3),axis = 0)
    
        d= np.concatenate((A,a),axis = 1)
        #e = c[::-1] ###########create symmetric of c on right side
    
        e = np.flip(d,0)
        

        f = np.concatenate((d,e))
        print ("f = ")
        
        
        f = np.delete(f,n,axis=1)
        f = np.delete(f,n,axis=0)
        print(f)
        print("************")
       
    else:
        if n ==1:
            #f = np.arange(1,1)
            f = np.eye(n, dtype=int)
            #print(f)
   
    return (f)

def main():

    print(diamond(11))
    pass

if __name__ == "__main__":
    main()
