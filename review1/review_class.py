from my_abc import ABCReview
import sys
import json

class NumberFun(): # no special inheritance
# class NumberFun(ABCReview):
    __slots__ = ('__n',) # these slots need to be in the highest hierachy
    def __init__(self, num):
        self.n = num # use the setter method
    def __str__(self):
        return f'''The {self.findEvenOdd()} number {self.n} squared is {self.findSquare()}
and the square root of {self.n} is {self.findSqrt()}
It is {self.findIfSquareNum()}''' # use the accessors
    def findSquare(self):
        return self.__n ** 2
    def findSqrt(self):
        return self.__n ** 0.5
    def findEvenOdd(self):
        return 'even' if self.n%2 == 0 else 'odd'
    def findIfSquareNum(self):
        r = self.findSqrt()
        if r==int(r):
            return 'a square number'
        else:
            return 'not a square number'
    @property
    def n(self):
        return self.__n
    @n.setter
    def n(self, num):
        if type(num) == int and num > 0:
            self.__n = num
        else:
            self.__n = 1 # sensible default

def main():
    '''run the code'''
    # if there is an extra system argument, use it for n
    if len(sys.argv)>1:
        ''' use system arguments as the value for 'n' '''
        n = int(float(sys.argv[1]))
    # Otherwise if there is a file called config.json load it
    else:
        try:
            fin = open('review1\\config.json', 'rt')
            struct = json.load(fin)
            n = struct['n']
            fin.close()
        except FileNotFoundError as fnf:
            n=100 # just set a sensible default
    print(f'Using n={n}:')
    r = NumberFun(n)
    # can we assign additional arbitrary properties?
    print(r)
    # r.__ooblywoobly = 'dumdedodeda'
    # print(r.__ooblywoobly)
    # can we access name-mangled properties?
    # print( r.__num ) # fails
    # r.__n = 99
    print(r.n) # calls the getter method of the class

if __name__ == '__main__':
    main()