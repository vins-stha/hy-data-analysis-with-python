#!/usr/bin/python3

import numpy as np

def almost_meeting_lines(a1, b1, a2, b2):
    
    A =np.array([[(-a1),1],[(-a2),1]])# y=a1x+b1 and y=a2x+b2. ==>> -ax1 + y = b1__________-ax2 + y = b2
    b = np.array([[b1],[b2]])

  #  print("a1={} : ,b1 = {},a2={},b2={}".format(a1,b1,a2,b2))
    results = np.linalg.lstsq(A,b,rcond=None)
   
    x,y = results[0]
    #x,y = x[0],y[0]
    
    
    exact = results[2]
    print("exct ",type(exact), exact)
    if exact==1:
        exact = False
    else:
        exact = True
    print("{:.6f} {:.6f} {}".format(x[0],y[0], (exact)))
    
    return ((x[0],y[0]),results)

def main():
    a1=1
    b1=2
    a2=-1
    b2=0
    a1=1
    b1=4
    p=(a1,b1,a1,b1+1)
   
    #results = almost_meeting_lines(1, 4, 3, 2)
    
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    (x, y), exact = almost_meeting_lines(*p)
    """if exact:
        print(f"Lines meet at x={x} and y={y}")
    
    a1=a2=1
    b1=2
    b2=-2
    (x, y), exact = almost_meeting_lines(1, 4, 1, 5)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b1)
    #(x, y), exact = almost_meeting_lines(1, 4, 1, 4)

    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")
    
    a1=1
    b1=2
    a2=1
    b2=1
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")
    
    """
if __name__ == "__main__":
    main()
