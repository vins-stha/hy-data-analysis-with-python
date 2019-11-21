#!/usr/bin/env python3

import pandas as pd

def main():
    #df = pd.read_csv("src\insurance.csv")

    try:
        df = pd.read_csv("src/municipal.tsv",sep="\t")
        cols_name = list(df.columns.values)
        r,col = df.shape
        #print("lenddd",df.head())
        print("Shape: {}, {}".format(r,col))
        print("Columns:")
        for i in range(0,len(cols_name)):
            print("{}".format(cols_name[i]))
            pass
        
    except:
        Exception
        print("could not load")
    return


if __name__ == "__main__":
    main()
