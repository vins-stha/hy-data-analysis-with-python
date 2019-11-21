
def reverse_dictionary(d):
    reverse={}

    for key,values in d.items():
        for value in values:
            reverse.setdefault(value,[]).append(key)
            #print(reverse)
    #print(reverse)

    return (reverse)


      
def main():
        

        d={'move': ['liikuttaa'], 'hide': ['piilottaa','salata'], 
        'six': ['kuusi'], 'fire': ['kuusi']}

        print(reverse_dictionary(d))

