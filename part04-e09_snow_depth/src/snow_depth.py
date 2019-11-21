#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    df = pd.read_csv("src/kumpula-weather-2017.csv")#, sep="\t")
    return df["Snow depth (cm)"].max()
    #return 0.0

def main():
    d = snow_depth()
    print("Max snow depth: {:.1f}".format(d))
    return

if __name__ == "__main__":
    main()
