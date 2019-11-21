#!/bin/python3
from functools import reduce
import numpy as np
a = [[1,0], [0,1]]

a = np.array([[1,2], [3,4]])

n = 4

c = ([d[:] for d in a] for i in range(n))
r = reduce(lambda a, b: [
    [a[0][0]*b[0][0]+a[0][1]*b[1][0], a[0][0]*b[0][1]+a[0][1]*b[1][1]],
    [a[1][0]*b[0][0]+a[1][1]*b[1][0], a[1][0]*b[0][1]+a[1][1]*b[1][1]]
], c)
print(r)
