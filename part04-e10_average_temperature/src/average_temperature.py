#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df = pd.read_csv("src/kumpula-weather-2017.csv")#, sep="\t")
    july_df = df.loc[df["m"]==7,:]

    return july_df["Air temperature (degC)"].mean()

def main():
    avg = average_temperature()
    print("Average temperature in July: {:.1f}".format(avg))
    return

if __name__ == "__main__":
    main()
