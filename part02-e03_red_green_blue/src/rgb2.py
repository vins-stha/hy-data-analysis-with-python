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
    print(len(Lines))
    ################################333
    
    for i in range(1,len(Lines)):
        matches=re.findall(pattern,Lines[i])
        matches_found=[]
        for items in matches:
            #print("items >>{}, len>>{}".format(items,len(items)))
            pass
            #for i in range (len(items)):
              #  print("index =={} item>>{}".format(i,items[i]))
              #pass
            r = matches_found.append('\t'.join([items[0],items[2],items[4],items[6]]))
           
            results.append(str(r))
            print(("***",matches_found,"**"," on split>>",type(r)))
##########3r type?????????????????????????????????????????            

    for i in range(len(matches_found)):
        print(" str>>",matches_found[i]," lend >>",len(matches_found[i]))
    print(len(results))
       
    return matches_found
   
  


def main():
    filename ="src/rgb.txt"
    (red_green_blue(filename))
    

if __name__ == "__main__":
    main()
