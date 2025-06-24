# reduce lets us repeatedly apply a function to reduce a quantity of values down to a single result
from functools import reduce
import sys
sys.path.append('D:\\pythonAdvancedJune2025\\utilities')

from util import addThem

def main():
    '''use reduce to add a load of numbers'''
    # here is a large quantity of values
    v = range(0, (10**9)+1, 2) # start, stop-before, step
    total= reduce( addThem, v )
    return total

if __name__ == '__main__':
    t = main()
    print(t)
