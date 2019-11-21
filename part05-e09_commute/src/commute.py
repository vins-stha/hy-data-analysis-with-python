#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from bicycle_timeseries  import bicycle_timeseries

#module_name="src.bicycle_timeseries"
#bicycle_timeseries = load(module_name, "bicycle_timeseries")
def commute():
    return None
    
def main():
    df = bicycle_timeseries()
    print("your df is ", df.head())
    return


if __name__ == "__main__":
    main()
