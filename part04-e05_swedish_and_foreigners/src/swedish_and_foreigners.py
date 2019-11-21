#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    try:
        df = pd.read_csv("src/municipal.tsv", sep="\t")
        df = df.loc[1:,:]
        df.set_index("Region 2018",inplace = True) 
        df = df.loc["Akaa":"Äänekoski",:]
        #print(df.shape)
        df = df.loc[((df.iloc[:,2])>5),:]
        df = df.loc[((df.iloc[:,3])>5),:]
        #cols = df.columns
        #print(type(cols))
        #for i in range(len(cols)):

         #   print("",i,"",cols[i])
        
        #print(df.shape)
        #cols = [0,2,3]
        #cols = df.columns[df.columns.isin([0,2,3])]

        #print(cols)
        df = df.iloc[:,[0,2,3]]
       # print(" headdddddddddd\n",df.head())
    except:
        Exception
        print("Something went wrong")
    return df

def main():
    swedish_and_foreigners()
    return

if __name__ == "__main__":
    main()
