# some useful utilities for general use

def squareIt(a):
    '''return the square of a'''
    return a**2


def isOdd(w):
    '''return True if odd, false otherwise'''
    return w%2 !=0

def addThem(m,n):
    '''add the two values and return the total'''
    return m+n

# When a module is imported,
# Python always assigns __name__ to the module name
print(__name__) # __main__

if __name__ == '__main__':
    print(isOdd(4)) # False