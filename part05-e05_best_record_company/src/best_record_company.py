#!/usr/bin/env python3

import pandas as pd
def myfilter(df):                                     # The filter function must return a boolean value
    return df["WoC"].sum() >= 10
def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    #print(df.head())

    publishers = df.groupby("Publisher")

    v = publishers["WoC"].apply(lambda x:(x.sum())).sort_values(ascending=False)
    result = df.loc[df["Publisher"]==v.index[0]]

    
    return result

def main():
    (best_record_company()) 
    return
    

if __name__ == "__main__":
    main()
