#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    #def integers_in_brackets(s):
    y = re.findall(r'\[\s*([+-]?\d+)\s*\]',s)
    return(list(map(int, y)))
    #"""regex = #(r"[\s-?][^aA-zZ]+[\d]")
    
   # print(test1)
   # res =re.findall(r"[\s]?[^aA-zZ+][-\d]+",s)
    #test1 = re.findall(r".?\d+.",s)
    #print(test1)
    ###alpha =["a",'b','c']
    """res = list(map(int, res))
    for i in range(len(test1)):
    #for items in test1:
        if "+" in test"""  """1[i] and"-" in test1[i]:
            test1.remove(test1[i])

        if "["  in test1[i]:
            print("before >>",test1[i])
            test1[i]= test1[i].replace("[","")
            print("after>>",test1[i])
        if "]" in test1[i]:
            #items= items.replace("+","")
            test1[i]= test1[i].replace("]","")
        if "+" in test1[i]:
            if test1[i][0]=="+":

                test1[i]= test1[i].replace("+","")
            if test1[i][-1]=="+":
                test1[i]=""
        if "a" in test1[i]:
             test1[i] = ""
        else:
           pass
        if " " in test1[i]:
            if test1[i][-1]== " ":
                test1[i]= test1[i].replace(" ","")
            else:
                pass
        


    test1 = list(filter(None,test1))
   # print(test1)            
    #print(type(res))
    print("final -->",test1)   
    return((res))
    """
    
    

def main():
  #  s="  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx"
   # s2=" afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xx"
    s = " afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx!"
   # s=""
    #s=" afd [asd+] [47 ] [a34]  [ +-43 ]tt [+12]xxx!"
    integers_in_brackets(s)
    #integers_in_brackets(s2)
   # print("**{}**>>>>{}".format(s,integers_in_brackets(s)))
    #print("**{}**>>>>{}".format(s2,integers_in_brackets(s2)))
    
if __name__ == "__main__":
    main()
