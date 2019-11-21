#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):

   # pattern = "(\d{1,3})+(\s+\w+.\w.*)"
    filename ="src/rgb.txt"
    matches,Lines,results,matches_found = [],[],[],[]

    f = open(filename)
    pattern=re.compile(r"(\d+)(\s+)(\d+)(\s+)(\d+)(\s+)(\w+.*)")
    line = f.readline()
    while line:    
        Lines.append(line) #append line to Lines list         
        line = f.readline() #read next line 
    f.close()
   
    matches_found=[]
    for i in range(1,len(Lines)):
        matches=re.findall(pattern,Lines[i])
       
        for items in matches:
            
            item = '\t'.join([items[0],items[2],items[4],items[6]])
           
            results.append(item)
  
       
    return results
  


def main():
    filename ="src/rgb.txt"
    print(red_green_blue(filename))
    pass

if __name__ == "__main__":
    main()























""" #!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    pattern = "\d+\s+[\w\s]+"
    pattern = "\d+\s+\w+"
    filename ="src/rgb.txt"
    line1="211 211 211		LightGray
    line2="25  25 112		midnight blue"
 #25  25 112		MidnightBlue
    line3="0   0 128		navy"
 # 0   0 128		navy blue"
    matches = []
    #txt = "199  21 133 		medium violet red"
   
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
        matches = re.findall(pattern,line1)
        #print(matches)
        
        for i in range(len(matches)):
            matches[i]=matches[i].replace(" ","\t")
            matches[i] = matches[i].replace("\n","")
            matches[i] = matches[i].replace("\t\t","\t")
            matches[i] = matches[i].replace("\t\t\t","\t")
            
            #print(matches)
            #print()
            FINAL.append(matches[i])
    print("length ",len(FINAL))
      

    return FINAL


def main():
    filename ="src/rgb.txt"
    print(red_green_blue(filename))
    pass

if __name__ == "__main__":
    main()
 """