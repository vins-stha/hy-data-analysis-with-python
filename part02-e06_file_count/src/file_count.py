#!/usr/bin/env python3
"""
Create a function file_count that gets a filename as parameter and returns a triple of numbers. The function should
 read the file, count the number of lines, words, and characters in the file, and return a triple with these count
  in this order. You get division into words by splitting at whitespace. You don’t have to remove punctuation.

Part 2.

Create a main function that in a loop calls file_count using each filename in the list of command line parameters 
sys.argv[1:] as a parameter, in turn. For call python3 src/file_count file1 file2 ... the output should be

?      ?       ?       file1
?      ?       ?       file2
...
The fields are separated by tabs (\t). The fields are in order: linecount, wordcount, charactercount, filename.
"""
import sys

def file_count(filename):
    filename = "src/test.txt"
   # test = "Create a main function that in a loop calls file_count using each filename in the list of command line parameters "
    charsList,wordsList = [],[]
    wordCount = 0

    with open(filename,"r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.split("\n")
         
    linesCount = len(lines) 
    for i in range(linesCount):
        words = lines[i].split()
        wordCount += len(words)
        #wordsInLine=(lines[i].split())
        #wordsList.append(wordsInLine)
        for chars in lines[i]:
           
            chars = chars.split()
            charsList.append(chars)
   
    charsCount = len(charsList)

    
    
    #print(linesCount, charsCount, wordCount)
    

    return (linesCount, wordCount,charsCount)

def main():
    filename = sys.argv[1:]
    results = []
    for i in range(len(filename)):
        results = file_count(filename)
        print("{}\t{}\t{}\t{}\t".format(results[0],results[1],results[2],filename[i]))
        pass

if __name__ == "__main__":
    main()
