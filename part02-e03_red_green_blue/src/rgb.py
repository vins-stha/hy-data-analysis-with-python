#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    pattern = "\d+\s+[\w\s]+"
    attern = "\d+\s+\w+"
    filename ="src/rgb.txt"
    matches = []
    #txt = "199  21 133 		medium violet red"
    line1="211 211 211		LightGray"
    line2="25  25 112		midnight blue"
 #25  25 112		MidnightBlue
    line3="0   0 128		navy"
    f = open(filename)
    line = f.readline()
    Lines =[]

    while line:
    
        Lines.append(line) #append line to Lines list
         
        line = f.readline() #read next line 

    f.close()
   
    FINAL = []
    #print("total lines ",len(Lines))
    for i in range(1,len(Lines)):
        #print(Line[i])
        matches = re.findall(pattern,Lines[i])
        #matches = re.findall(pattern,line1)
        matches = (str(matches))
        part2 = matches[14:]
        part1 = matches[:13]
        part1 = part1.replace("\\","")
        part1 = part1.replace("t","")
        part2 = part2.replace("\\n","")
        
        if "t\\t"  in part2:
         
            part2= part2.replace("t\\t","")
        if"\\t" in part2:
            part2 = part2.replace("\\t","")
        if part2[0]=="t":
            part2 = part2[1:]
        
        part1 = " ".join(part1.split())
        part1 = part1.replace(" ","\\t")
        total = part1+"\\t"+part2
        #print(part1,"**",part2,"**",total)      
        FINAL.append(total)
        
    print(len(FINAL))

    return FINAL


def main():
    filename ="src/rgb.txt"
    print(red_green_blue(filename))
    pass

if __name__ == "__main__":
    main()
