#!/usr/bin/env python3

import sys
import math

def summary(filename):
    numList =[]
    
    with open(filename, "r") as file:
        line = file.readlines()
        for nums in line:
            nums = nums.strip("\n")
            #numList.append(nums)
            try:
                nums=float(nums)
                numList.append(nums)
        
            except ValueError:
                print("NAN")
                pass 
                
    #file.close()
    #numList = [float(nums) for nums in numList]

    sum,sum1 = 0.0,0.0
    for items in numList:
        sum +=items
  
    avg = (sum/len(numList))
     
    for nums in numList:
        sum1 += (nums-avg)**2
    sd = math.sqrt(sum1/(len(numList)-1))
    
    
    return (sum,avg,sd)
 
def main():
    filenames = sys.argv[1:]
    #print("FILEL>>>",filename)
    for filename in filenames:
        results = summary(filename)
    
        print("File: {} Sum: {:.6f} Average: {:.6f} Stddev: {:.6f}".format(filename,results[0],results[1],results[2]))
    
    
     
    
if __name__ == "__main__":
    main()
