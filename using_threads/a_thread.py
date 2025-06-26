from threading import Thread
import time

# every additional thread shares the same python instance, the same memory and data as the main thread

def fn():
    '''any function may be invoked on a new thread'''
    # emulate a long running piece of code
    time.sleep(1)
    print(f'this is the function')

if __name__ == '__main__':
    '''use threading'''
    start = time.time()
    # fn()
    # fn()
    # fn()
    # fn()
    tA = Thread(target=fn)
    tB = Thread(target=fn)
    tC = Thread(target=fn)
    tD = Thread(target=fn)
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