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
    fn()
    fn()
    fn()
    fn()
    end = time.time()
    print(f'Total operation: {end-start}') # about 4 seconds