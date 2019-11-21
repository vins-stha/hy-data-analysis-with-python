#!/usr/bin/env python3
"""
Write function file_extensions that gets as a parameter a filename. It should read through the lines from this file. 
Each line contains a filename. Find the extension for each filename. The function should return a pair, where the first
 element is a list containing all filenames with no extension (with the preceding period (.) removed). The second
  element of the pair is a dictionary with extensions as keys and corresponding values are lists with filenames having 
  that extension.

Sounds a bit complicated, but hopefully the next example will clarify this. If the file contains the following lines

file1.txt
mydocument.pdf
file2.txt
archive.tar.gz
test
then the return value should be the pair: (["test"], { "txt" : ["file1.txt", "file2.txt"], "pdf" :
 ["mydocument.pdf"], 
"gz" : ["archive.tar.gz"] } )
"""

def file_extensions(filename):
    dictionary = dict()
    dict_tuple = tuple()
    wordsList,noExt = [],[]
    with open(filename,"r") as file:
        lines = file.readlines()
        #print(len(lines))
        for i in range(len(lines)):
            lines[i]=lines[i].strip("\n")
            if "." in lines[i]:
                words = lines[i].rsplit(".",1)
                wordsList.append(words)
            else:
                noExt.append(lines[i])
               # print(len(noExt))
        for items in noExt:
            if items=="":
                noExt.remove(items)
     

        #print(wordsList,len(wordsList))
  
        for words in wordsList:
            temp =""
            temp = words[-1]
            words[-1] = words[0]
            words[0] = temp
       
            dictionary.setdefault(words[0],[]).append(words[-1]+"."+words[0])
         
           
       # print(dictionary)
        
    return (noExt, dictionary)

def main():
    filename ="filenames.txt"
    result=[]
    result = file_extensions(filename)
    #print(result)
   # End of part 1
  
    numOfnoEx = len(result[0])
    if numOfnoEx==0:
        print("0 files with no extension")
    else:
        print("{} files with no extension".format(numOfnoEx))
    
  #  key = sorted(result[1].keys())

  
    for key, value in sorted(result[1].items()):
        print (("{} {}").format(key, len(result[1][key])))

   

if __name__ == "__main__":
    main()
