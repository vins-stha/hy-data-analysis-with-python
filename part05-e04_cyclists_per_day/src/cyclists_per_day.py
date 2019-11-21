#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

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
def clean_cyclist():
    cyclist = pd.read_csv("src/Helsingin_pyorailijamaarat.csv",sep=";")
    cyclist.dropna(how="all",inplace = True)
    dates = split_date(cyclist)
    cyclist = cyclist.drop("Päivämäärä",axis=1)
    df_cyclist = pd.concat([dates,cyclist],axis=1)
    df_cyclist = df_cyclist.drop("Unnamed: 21",axis = 1)
    
    return df_cyclist

    
    
def cyclists_per_day():
    cleaned_data = clean_cyclist()
    cleaned_data = cleaned_data.drop(["Hour","Weekday"],axis=1)
    grouped = cleaned_data.groupby(["Year","Month","Day"])

  #  print(grouped.sum().head())
    return grouped.sum()
    
def main():
    data = cyclists_per_day()
  #  print(data.tail())
    try:
       # data_aug = data.loc[(data.loc["Month"]==8 & data.loc["Year"]==2017),:]
        data2 = data.groupby(["Month"])
        all_aug = data2.get_group(8)
        aug = all_aug.groupby(["Year"])
      
        aug_2017 = aug.get_group(2017)
       
       
        aug_2017.plot()
        plt.show()
    except ValueError as e:
        print("ERROR >>>>",e)
    #print(data_aug)
    return

if __name__ == "__main__":
    main()
