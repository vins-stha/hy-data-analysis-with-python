#!/usr/bin/env python3

import pandas as pd

def top_bands():
    bands = pd.read_csv("src/bands.tsv",sep="\t")
    uk = pd.read_csv("src/UK-top40-1964-1-2.tsv",sep="\t")
    bands["Band"] =[a.capitalize() for a in bands.Band]
    uk["Artist"] = [a.capitalize() for a in uk.Artist]

    uk_top = pd.merge(uk,bands, right_on="Band", left_on="Artist")
   # print(uk_top.head())



    return uk_top
def main():
    top_bands()
    return

if __name__ == "__main__":
    main()
