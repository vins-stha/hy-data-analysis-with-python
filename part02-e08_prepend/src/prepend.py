#!/usr/bin/env python3

class Prepend(object):
    def __init__(self,start):
        self.start= start
        #print(start)
    def write(self,strings):

        print(self.start + strings)

    # Add the methods of the class here

def main():
    p = Prepend("+++ ")
    p.write("Hello ")
    pass

if __name__ == "__main__":
    main()
