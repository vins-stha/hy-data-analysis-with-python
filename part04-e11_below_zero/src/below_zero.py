#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    zero = df.loc[df["Air temperature (degC)"]<0]
    zero_days = zero.shape[0]
  #  print(zero.head())
    return zero_days

def main():
    zero = below_zero()
    print("Number of days below zero: ",zero)
    return
    
if __name__ == "__main__":
    main()
