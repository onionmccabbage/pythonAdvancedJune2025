import sys
# we may append a shared location for everyone to use common code
sys.path.append('d:\\pythonAdvancedJune2025\\utilities')

from using_fn.util import squareIt
from using_fn.util import isOdd
from using_fn.util import addThem

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
    # we use the filter object like this
    odd_nums = [i for i in odds]
    print(odd_nums)


    # we may be working with very large amounts of data
    print(10**1024)
    big = range(0,10**1024) # this creates a map object - the values are yielded when needed
    big_sq = map(squareIt, big)
    print( big_sq.__next__() )# 0
    print( big_sq.__next__() )# 1
    print( big_sq.__next__() )# 4
    

# when we run a module directly, 
# Python will always assign __name__ to __main__
print(__name__) # __main__

if __name__ == '__main__':
    main()