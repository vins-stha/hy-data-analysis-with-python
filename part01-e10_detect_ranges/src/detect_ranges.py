#!/usr/bin/env python3

def detect_ranges(L):
    x = sorted(L)
    result = []

    while len(x)>0:
        i = x[0]
        s =[i]
        x = x[1:]

        while len(x)>0 and x[0]==i+1:
            s.append(x[0])
            i = x[0]
            x = x[1:]
        if len(s)==1:
            result.append(s[0])
        else:
            result.append((min(s),max(s)+1))
    return((result))

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    print(detect_ranges(L))
   

if __name__ == "__main__":
    main()
