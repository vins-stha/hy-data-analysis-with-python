#!/usr/bin/env python3-

import pandas as pd

def subsetting_with_loc():
    df_original = pd.read_csv("src/municipal.tsv", index_col="Region 2018", sep ="\t")
  
    df_final= df_original.loc["Akaa":"Äänekoski",
                                ["Population","Share of Swedish-speakers of the population, %",
                                "Share of foreign citizens of the population, %"
                                ]
                            ]
  
    return df_final

def main():
   
    subsetting_with_loc()
 
    return

if __name__ == "__main__":
    main()
