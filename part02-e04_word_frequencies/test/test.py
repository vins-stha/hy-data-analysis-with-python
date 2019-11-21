def freq(str): 
  
    # break the string into list of words 
    str_list = str.split() 
  
    # gives set of unique words 
    unique_words = set(str_list) 
    print(set(str_list))
      
    for words in unique_words : 
        print('Frequency of ', words , 'is :', str_list.count(words)) 
  
# driver code 
if __name__ == "__main__": 
      
    str ='apple Apple mango apple orange orange apple guava mango mango'
      
    # calling the freq function 
    freq(str) 