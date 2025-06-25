import doctest

def square(n=3):
    '''return the square of n
    >>> square(2)
    4
    >>> square(-3)
    9
    >>> square()
    9
    '''
    return n**2

if __name__ == '__main__':
    c = square(8)
    print(c)
    doctest.testmod(verbose=True)