#!/usr/bin/env python3
import pandas as pd
import re

def read_series():
    dataList,indices = [],[]
    pattern =r"^[aA-zZ]+(\s)+[0-9]+"
   
    while True:
      
        data = input("Enter index and data : ")
        if re.match(pattern, data):
                
            data2 = re.split(r'\s+',data)
                
            indices.append(data2[0])
                
            dataList.append(data2[1])
                
        elif data =="":
            break
           
        
        else: #(re.match(pattern, data))==False:
            raise Exception("malformed input")


    pd_series = pd.Series(dataList, index=indices, dtype = object)
    print(pd_series)        
    return pd_series

def main():
    read_series()
    pass

if __name__ == "__main__":
    main()
