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
    
    
   
def cycling_weather():
    cyclist = pd.read_csv("src/Helsingin_pyorailijamaarat.csv",sep=";")
    weather = pd.read_csv("src/kumpula-weather-2017.csv",sep=",")
    
    cyclist.dropna(how="all",inplace = True)
    dates = split_date(cyclist)
    cyclist = cyclist.drop("Päivämäärä",axis=1)
    
    df_cyclist = pd.concat([dates,cyclist],axis=1)
    
    df_cyclist = df_cyclist.drop("Unnamed: 21",axis = 1)
   
    final = pd.merge(weather,df_cyclist, left_on = ["Year","m","d"], right_on=["Year","Month","Day"])
    final = final.drop(["m","d","Time","Time zone"], axis = 1)
   
    return final

def main():
    df = cycling_weather()
    print(df.shape, df.columns)

    return

if __name__ == "__main__":
    main()
