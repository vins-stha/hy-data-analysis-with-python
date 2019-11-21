#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
   # print(s)
    s2 = pd.Series([index for index in s.index],  index = [value for value in  s.values])
    #print(s2)

    return s2

def main():
    L=[1,2,3,1]
    ind=list("abcd")
    s = pd.Series(L, index=ind)

    inverse_series(s)
    return

if __name__ == "__main__":
    main()
