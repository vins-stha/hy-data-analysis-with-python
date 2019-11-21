#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():

    
    data = { "State":["United Kingdom","Finland","USA","Sweden","Germany","Russia"],
        "Year of independence":[np.nan,1917,1776,1523,np.nan,1992],
        "President":[np.nan,"Niinistö","Trump",np.nan,"Steinmeier","Putin"]
       }
                      
    df = pd.DataFrame(data)
    df.astype({"State":"object", "Year of independence":"float"}).dtypes

    df.set_index("State",inplace=True)
   
    #print(df)

#    a = np.testing.assert_array_equal(df.columns, ["Year of Independence", "President"],
 #       err_msg="Incorrect column names!")
  #  print(a)

    return df
               
def main():
    a = missing_value_types()
   # print(a.columns)
    #return

if __name__ == "__main__":
    main()
