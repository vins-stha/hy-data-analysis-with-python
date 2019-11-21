#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):

    rowsList = []
    for rows in a:
        rowsList.append(rows.reshape(1,np.shape(a)[1]))
       # print("rows :: ",rows)
    return rowsList

def get_column_vectors(a):###
    #print("type = ",type(a))
   # print(np.ndim(a), np.shape(a))
    a = a.T
    columnsList = []
   
    for cols in a:
        col = cols.reshape(np.shape(a)[1],1)
        columnsList.append(col)
   
    return (columnsList) 


def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,5))
    a = np.random.randint(0, 100, (3, 5))

    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
