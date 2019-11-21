#!/usr/bin/env python3

import pandas as pd
import numpy as np
"""
1. the format (names of rows/columns) of the last week's list should be the 
  same as on this week's list - right?
2. where on last week's list you should put the values on this week's list's column "LW"? 
  are all the values valid?
3. what do you know (if anything?) about values on last week's column "LW"?
4. if you don't know the song that was, for example, on place 6, what should be the values on
   that line?
"""

def last_week():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df["LW"].replace(["Re","New"],np.NaN, inplace=True)
    df["LW"]=pd.to_numeric(df["LW"])
    df.loc[df.isnull().any(axis=1), :] = np.nan

    df.sort_values("LW",ascending=True,inplace = True)

    print(
        
    )

    return df

def main():
    df = last_week()
  #  print("Shape: {}, {}".format(*df.shape))
   # print("dtypes:", df.dtypes)
    #print(df)


if __name__ == "__main__":
    main()
