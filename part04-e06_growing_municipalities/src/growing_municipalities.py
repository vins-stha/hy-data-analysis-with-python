#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    df_municipals = df["Akaa":"Äänekoski"]
    #print(df_municipals.shape)
    df_growing = df_municipals.loc[((df_municipals.iloc[:,1])>0),:]
    
    return  (df_growing.shape[0]/df_municipals.shape[0])
    

def main():
    df = pd.read_csv("src/municipal.tsv", index_col = 0, sep  ="\t")
    a = growing_municipalities(df)
    print("Proportion of growing municipalities: {:.1f}%".format(a*100))
    
    return

if __name__ == "__main__":
    main()
