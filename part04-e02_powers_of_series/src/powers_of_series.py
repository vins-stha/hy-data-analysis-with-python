#!/usr/bin/env python3

import pandas as pd
import numpy as np

def powers_of_series(s, k):
    """ k= num of cols"""
   
    cols_name= list(range(1,k+1))
    row_name = s.index
  
    data = list(s.values**i for i in (range(1,len(cols_name)+1 )))
    data = np.transpose(data)

   
    df = pd.DataFrame(data,index=row_name,columns = cols_name) 
 
    #print(df)

    return df
    
def main():
 
    ind=list("abcdefghijklmnopqrstuvwxyz")
    k=3
    for n in range(4):
        L=np.random.randint(-10, 10, n)
        s = pd.Series(L, index=ind[:n])
   
        powers_of_series(s, k)
   
    return
    
if __name__ == "__main__":
    main()
