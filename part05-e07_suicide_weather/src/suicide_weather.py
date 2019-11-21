#!/usr/bin/env python3

import pandas as pd
import numpy as np
def suicide_fractions():
    df_suicide = pd.read_csv("src/who_suicide_statistics.csv",sep=",", index_col="country")
    df_suicide.index.names = ['Country']
    try:
       
        grouped_data = df_suicide.groupby("Country")["suicides_no"].apply(lambda x: np.mean(x.div(df_suicide
                                ["population"])))
        grouped_data = grouped_data.to_frame()
       
    except Exception as e:
        print(e)
    return grouped_data
 
    
def suicide_weather():
    #df_suicide = pd.read_csv("src/who_suicide_statistics.csv",sep=",", index_col="country")
    grouped_data = suicide_fractions()
    print(grouped_data.tail())
    df_country = pd.read_html("src/List_of_countries_by_average_yearly_temperature.html", index_col="Country", header=0)
    
    df_country[0].index.sort_values()
    df_country[0].index = df_country[0].index.sort_values()
        
    s = df_country[0].values
    #print(df_country[0].tail(10))
    for i in range(0,len(df_country[0].values)):
      
        if "\u2212" in df_country[0].values[i][0]:
            #print("before >>",s[i][0])
            s[i][0].replace("\u2212", "-")
        else:
            s[i][0]=float(s[i][0])
    #"""
    df  = merged_data = pd.merge(df_country[0],grouped_data,on="Country")
   # print(df.tail(10))
    print(df.suicides_no.corr(df['Average yearly temperature (1961–1990, degrees Celsius)'],method = "spearman"))
    ser1 =pd.Series(df['suicides_no'].values, index=df.index.values)
    ser2 =pd.Series(df['Average yearly temperature (1961–1990, degrees Celsius)'].values, index=df.index.values)
    cor = ser1.corr(ser2, method="spearman")
    print(cor)
    return (grouped_data.shape[0], df_country[0].shape[0], df.shape[0], cor)

def main():
    results = suicide_weather()
  #  print(results)
    print("Suicide DataFrame has ",results[0]," rows")
    print("Temperature DataFrame has ",results[1]," rows")
    print("Common DataFrame has ",results[2]," rows")
    print("Spearman correlation: ",results[3])
    
    return

if __name__ == "__main__":
    main()
