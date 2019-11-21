#!/usr/bin/env python3
""" The file src/listing.txt contains a list of files with one line per file. Each line contains seven fields: access rights, number of references, owner’s name, name of owning group, file size, date, filename. These fields are separated with one or more spaces. Note that there may be spaces also within these seven fields.

Write function file_listing that loads the file src/listing.txt. It should return a list of tuples (size, month, day, hour, minute, filename). Use regular expressions to do this (either match, search, findall, or finditer method).

An example: for line

-rw-r--r-- 1 jttoivon hyad-all   25399 Nov  2 21:25 exception_hierarchy.pdf
the function should create the tuple (25399, "Nov", 2, 21, 25, "exception_hierarchy.pdf"). """


import re


#def file_listing(filename="src/listing.txt"):
def file_listing(filename="src/listing.txt"):
    pat3 = "[\d]+\s[A-Z][a-z]+\s.\d+\s\d+:\d+\s[\w._-]+"
    resultant = []
    f = open(filename)
    line = f.readline()
    
    while line:
        #print (lyn)
        result = re.findall(pat3,line)
        for word in result:
            L,final = [],[]
            L = word.split()

            a,b,c = int(L[0]), L[1], int(L[2])
            time = L[3].split(":")
            d,e = int(time[0]), int(time[1])
            final.append(a)
            final.append(b)
            final.append(c)
            final.append(d)
            final.append(e)
            final.append(L[4])
            #print(final)
        resultant.append(final)
       
        line = f.readline()
    f.close()
    return resultant
   
   

def main():
    filename = "src/listing.txt"
   
    print(file_listing(filename))
    

if __name__ == "__main__":
    main()



"""
  #name = re.findall(r"([^\b- ][\d]+| [A-Z][a-z]+|[aA-zZ]*\.[a-z]+)",txt)
    #trial2 = re.findall(r"([^\b- :][\d]+|[A-Z][a-z]+|[aA-zZ]*\.[a-z]+)",txt)
    #trial3= re.findall(r"([^\b- :][\d]+|([A-Z][a-z][a-z]|  [\d])+|[a-z_]*\.[a-z]+)",txt)
    #listing = (re.findall(r"([\d]{2,}|[\s]+[A-Za-z]+\.[a-z]+)",txt))
   
"""