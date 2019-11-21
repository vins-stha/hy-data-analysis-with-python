#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv",sep=";")
    print(df.head())
    
    dates = df["Päivämäärä"].str.split(expand=True)
#    print(dates.head())
    #df.rename(index={0: "x", 1: "y", 2: "z"})
    dates.dropna(how="any",inplace = True)
    dates = dates.rename(columns = 
        {
            0 : "Weekday",
            1 : "Day",
            2 : "Month",
            3 : "Year",
            4 : "Hour"
        })
    dates["Weekday"]=dates["Weekday"].map({"ma":"Mon","ti":"Tue","ke":"Wed","to":"Thu",
                        "pe":"Fri","la":"Sat", "su":"Sun"

                        })
    dates["Month"]= dates["Month"].map({"tammi":1,"helmi":2,"maalis":3,
                                        "huhti":4,"touko":5,"kesä":6, "heinä":7,
                                        "elo":8,"syys":9,"loka":10,
                                        "marras":11,"joulu":12
                        })
    dates["Day"]= dates["Day"].astype(int)
    
    dates["Year"]= dates["Year"].astype(int)
        
    dates["Hour"]=dates["Hour"].str.replace(":00","")

    dates["Hour"]= dates["Hour"].astype(int)
   
   
    return dates

def main():
    split_date()
    return
       
if __name__ == "__main__":
    main()
