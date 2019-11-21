#!/usr/bin/env python3
"""
Create function word_frequencies that gets a filename as a parameter and returns a dict with the word frequencies.
In the dictionary the keys are the words and the corresponding values are the number of times that word occurred in 
the file specified by the function parameter. Read all the lines from the file and split the lines into words usin
g the split() method. Further, remove punctuation from the ends of words using the strip(""""#$%&'()*,-./:;?@[]_"""
 #method call.
"""Test this function in the main function using the file alice.txt. In the output, there should be a word and its
 count per line separated by a tab:

The     64
Project 83
Gutenberg   26
EBook   3
of      303
"""
import re
def word_frequencies(filename):
    file = open(filename,"r")
    dictionary = dict()
    
    for lines in file:
        words = lines.split(" ")
        
        for word in words:
            word = word.strip("""!"#$%&'()*,-./:;?@[]_\n""")
          
            
            if word in dictionary:
                dictionary[word] = dictionary[word]+1
            else:
                dictionary[word] = 1
           
  
    """  print("of ", di['of'],"AGAINST 303")
    print("The ",di['The'],"AGAINST 64")
    print("Project ",di['Project'],"AGAINST 83")
    print("Gutenberg ",di['Gutenberg'],"AGAINST 26")
    print("Rabbit ",di['Rabbit'],"AGAINST 28")
    print("Carroll ",di['Carroll'],"AGAINST 3") """
    #print("creating ",dictionary['creating'],"AGAINST 3")
    """  print("sleepy ",di['sleepy'],"AGAINST 2") """
    #print(len(dictionary),"AGAINST 2424")
    for word,count in dictionary.items():
        print("{}\t{}".format(word,count))    
        pass
       
       
  
    
    #print(dictionary)
        
    return dictionary

def main():
    filename="src/alice.txt"
    print(word_frequencies(filename))
    pass

if __name__ == "__main__":
    main()






