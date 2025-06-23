from util import squareIt
from util import isOdd
from util import addThem

# Python includes map and filter as useful functional features

def main():
    '''we often group our main code like this'''
    # using 'map' to apply a function across every member of a collection
    d = (4,6,2,8,5,3,1)
    squares = map(squareIt, d)
    print(squares, type(squares))
    # just as with range and generators, we may access the next member of a map object
    print( squares.__next__() ) # 16
    print( squares.__next__() ) # 36
    print( squares.__next__() ) # 4
    print('-----------------')
    # we may iterate over the map object
    for _ in squares:
        print(_) # we often use _ for an iterable we do not need to persist
    # NB the iterator ends when the map object is exhausted

    # we can use filter to apply a filter function across a collection  of data
    # only data members which pas the filter function  validation will end up within the results
    odds = filter(isOdd, d)
    print(odds, type(odds)) # a filter object

if __name__ == '__main__':
    main()