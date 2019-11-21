#!/usr/bin/env python3

class Rational(object):
    def __init__(self, num,den):
        self.num = (num)
        self.den = (den)
        
        
        
       
      # print(type(self.rational))
    def __str__(self):
        return str("{}/{}".format(self.num,self.den))
       
    def __add__(self,Rational2):
        result=Rational(1,1)
        result.num = (self.num*Rational2.den + Rational2.num*self.den)
        result.den = Rational2.den*self.den
        #print("{}/{} + {}/{} =={}/{}".format(self.num,self.den,Rational2.num,Rational2.den,result.num,result.den))
        return(result)

    def __sub__(self,Rational2):
        result = Rational(1,1)
        result.num = (self.num*Rational2.den - Rational2.num*self.den)
        result.den = Rational2.den*self.den
        #print("{}/{} - {}/{} ==".format(self.num,self.den,Rational2.num,Rational2.den))
        return(result)

    def __mul__(self,Rational2):
        result = Rational(1,1)
        result.num = (self.num*Rational2.num )
        result.den = Rational2.den*self.den
        #print("{}/{} * {}/{} =={}/{}".format(self.num,self.den,Rational2.num,Rational2.den,self.num,self.den))
        return(result)

    def __truediv__(self,Rational2):
        result = Rational(1,1)
        result.num = (self.num*Rational2.den )
        result.den = Rational2.num*self.den
        return(result)
    
    def __eq__(self,Rational2):
    
        return((self.num/self.den)==(Rational2.num/Rational2.den))
    def __gt__(self,Rational2):
        
        return((self.num/self.den)>(Rational2.num/Rational2.den))
    def __lt__(self,Rational2):
        
        return((self.num/self.den)<(Rational2.num/Rational2.den))
    
    


def main():
    r1=Rational(11,12)
    r2=Rational(-5,12)
    print(r1)
    print(r2)
    print(r1+r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))
    
if __name__ == "__main__":
    main()
