#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    df_original = pd.read_csv("src/UK-top40-1964-1-2.tsv",  sep ="\t")
    df_10 = df_original.iloc[:10,[2,3]]

    
    return df_10

def main():
    subsetting_by_positions()
    return

if __name__ == "__main__":
    main()
