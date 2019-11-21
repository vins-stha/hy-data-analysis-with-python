#!/usr/bin/env python3
import pandas as pd


def create_series(L1, L2):
    #print(L1,L2)
    indices = ['a','b','c']
    s1 = pd.Series(L1, index =indices)
    s2 = pd.Series(L2, index =indices)
   
    return (s1, s2)
    
def modify_series(s1, s2):
    s1["d"] =s2["b"]
      
    del(s2["b"])
    
    return (s1, s2)

def main():
    L1=[2,3,4]
    L2=[9,8,7]

    s1,s2 = create_series(L1,L2)
    s1,s2 = modify_series(s1,s2)
    s1+s2
   # print(s1.add(s2))
        
if __name__ == "__main__":
    main() 
