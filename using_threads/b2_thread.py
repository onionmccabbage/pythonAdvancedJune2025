from threading import Thread
import time
import timeit
import random

class SimpleClass(): # this may inherit from any other class
    '''This class will be callable on a new thread'''
    def __init__(self):
        pass # we might choose to pass in arguments for the class instance
    # if we write a __call__ method, this can be targeted in a new Thread
    def __call__(self, n):
        msg = ''
        for _ in range(0,4):
            msg += f'{n} is sleeping\n'
            time.sleep(random.random()*0.5)
        print(msg)

if __name__ == '__main__':
    # new threads can only target instances of our class
    sc = SimpleClass()
    start = timeit.default_timer()
    thread_list = []
    for _ in range(0,16):
        thread_list.append( Thread(target=sc, args=(_,))  )
    for _ in thread_list:
        _.start()
    for _ in thread_list:
        _.join()
    # t = Thread(target=sc, args=(1,))
    # t.start()
    # t.join()
    end = timeit.default_timer()
    print(f'Total execution time: {end-start} sec')