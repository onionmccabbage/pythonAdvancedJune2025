from threading import Thread
import time

# every additional thread shares the same python instance, the same memory and data as the main thread

def fn(n):
    '''any function may be invoked on a new thread'''
    # emulate a long running piece of code
    time.sleep(1)
    print(f'this is function {n}')

if __name__ == '__main__':
    '''use threading'''
    start = time.time()
    # fn()
    # fn()
    # fn()
    # fn()
    # if we wish we may pass a tuple of arguments into the function
    # we may also pass in a dict of keyword arguments
    tA = Thread(target=fn, args=(1,))
    tB = Thread(target=fn, args=(2,))
    tC = Thread(target=fn, args=(3,))
    tD = Thread(target=fn, args=(4,))
    # we need to start the threads
    tA.start()
    tB.start()
    tC.start()
    tD.start()
    # we may wish to wait for the other threads to complete before moving on with the main thread
    tA.join()
    tB.join()
    tC.join()
    tD.join()
    # this next line will only run when all the other threads have (re)joined the main thread
    end = time.time()
    print(f'Total operation: {end-start}') # about 4 seconds