#!/usr/bin/env python3

import pandas as pd
import numpy as np

def  capitalise(df):
    
    for i in range(len(df)):
        #try:
        if("," in df[i]):
            a = df[i].split(",")
           
            if a[0].istitle()==False:
                a[0] = a[0].strip()
                a[0] = a[0].capitalize()
            if a[1].istitle()==False:
                a[1] = a[1].strip()
                a[1] = a[1].capitalize()

                
            df[i] = a[1].strip()+" "+a[0]
        else:
            
            a = df[i].split(" ")
            if a[0].istitle()==False:
                a[0] = a[0].strip()
                a[0] = a[0].capitalize()
            if a[1].istitle()==False:
                a[1] = a[1].strip()
                a[1] = a[1].capitalize()
            df[i] = a[0].strip()+" "+a[1]

    return df



def clean_Seasons(df):
    for i in range(len(df)):

        try:
            if("one" in df[i]):
                df.replace("one",1)
               
            if("two" in df[i]):
                df = df.replace("two",2)
           
            if("three" in df[i]):
                df = df.replace("three",3)
               
        except:
            Exception
           
    return df

def cleaning_data():
    df = pd.read_csv("src/presidents.tsv", sep="\t")
    df["President"] = capitalise(df["President"])
    df["Vice-president"] = capitalise(df["Vice-president"])
    a = df["Start"][0].split(" ")
    df["Start"][0] =  a[0]
    df["Start"] =  df["Start"].astype(int)
    for i in range(len(df.Last)):
        try:
            df.Last[i] = float(df.Last[i])
        except:
            Exception
            df.Last[i] = np.nan
    df["Last"] = df["Last"].astype(float)

    df["Seasons"] = clean_Seasons(df["Seasons"])
    df["Seasons"] = df["Seasons"].astype(int)
    print(df, "\n")     
    return df

def main():
    cleaning_data()
 
    return

if __name__ == "__main__":
    main()
