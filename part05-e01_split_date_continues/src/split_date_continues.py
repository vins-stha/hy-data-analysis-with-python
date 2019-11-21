#!/usr/bin/env python3

import pandas as pd


def split_date(df):
    
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:, 0]
    
    d["Weekday"] = d["Weekday"].map({"ma":"Mon","ti":"Tue","ke":"Wed","to":"Thu",
                        "pe":"Fri","la":"Sat", "su":"Sun"

                        })
    d["Month"] = d["Month"].map({"tammi":1,"helmi":2,"maalis":3,
                                        "huhti":4,"touko":5,"kesä":6, "heinä":7,
                                        "elo":8,"syys":9,"loka":10,
                                        "marras":11,"joulu":12
                        })
    
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d

def split_date_continues():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv",sep=";")
    try:
        df.dropna(how="all",inplace = True)
        dates = split_date(df)
        df = df.drop("Päivämäärä",axis=1)
       # print(df.shape, dates.shape)
        df = pd.concat([dates,df],axis=1)
      #  print(df.head())
        df = df.drop("Unnamed: 21",axis = 1)
        #print(df.columns)
    except ValueError as e:
        print("Could not ",e)
    return df

def main():
    df = split_date_continues()
    print("Shape:", df.shape)
  #  print("Column names:\n", df.columns)
   # print(df.head())


if __name__ == "__main__":
    main()
