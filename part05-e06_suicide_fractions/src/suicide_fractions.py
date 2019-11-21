#!/usr/bin/env python3

import pandas as pd
import numpy as np

def suicide_fractions():

    df = pd.read_csv("src/who_suicide_statistics.csv")
    gp2 =df.groupby("country")["suicides_no"].apply(lambda x: np.mean(x.div(df["population"])))

   
    return gp2

def main():
    suicide_fractions()
    return

if __name__ == "__main__":
    main()
