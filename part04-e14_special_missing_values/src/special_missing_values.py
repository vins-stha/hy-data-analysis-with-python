#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df["LW"].replace(["Re","New"],np.NaN, inplace=True)

  
    df["LW"]=pd.to_numeric(df["LW"])
    #df.astype({"LW":"int64"})

    dropped_df = df.loc[df["Pos"]>df["LW"]]
    #print(dropped_df)

    return dropped_df

def main():
    special_missing_values()
    return

if __name__ == "__main__":
    main()
