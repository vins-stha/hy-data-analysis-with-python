#!/usr/bin/env python3

import scipy.stats
import numpy as np


def load2():
    """This loads the data from the internet. Does not work well on the TMC server."""
    import seaborn as sns
    return sns.load_dataset('iris').drop('species', axis=1).values

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    datas = load()
    a = sepal_length = [d for d in datas[:,0]]
    b = petal_length = [d for d in datas[:,2]]
    correlation = (scipy.stats.pearsonr(a, b))
   # print(scipy.stats.pearsonr(a,b)[0])       
    return correlation[0]

def correlations():
    datas = load()
    a = sepal_length = [d for d in datas[:,0]]
    b = sepal_width = [d for d in datas[:,1]]
    c = petal_length = [d for d in datas[:,2]]
    d = petal_width = [d for d in datas[:,3]]
    """  cors = []
    
    vars =[a,b,c,d] """
   
    """  for i in range(len(vars)):
        j=i+1
        for j in range(len(vars)):
            cors.append([scipy.stats.pearsonr(vars[i],vars[j])[0]])  """
        
    #result = np.array(cors).reshape(4,4)
    result2 = np.corrcoef([a,b,c,d])
    print(result2)
    
    return result2

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
