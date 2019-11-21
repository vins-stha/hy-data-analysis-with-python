#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    try:
        df = pd.read_csv("src/municipal.tsv",sep="\t")
        df2 = df.loc[1:,:]#excluding Country variable row
        df2.set_index("Region 2018", inplace = True)
        df_municipal = df2.loc["Akaa":"Äänekoski",:]
        
    except:
        Exception
    return df_municipal
    
def main():
    municipalities_of_finland()
    return
    
if __name__ == "__main__":
    main()
