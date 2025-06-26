from threading import Thread
import time
import random

class MyClass(Thread): # our class inherists from the Thread class
    '''Any class may inherit from Thread'''
    def __init__(self, n, x):
        # if we call super().__init__ we MUST provide all the required arguments
        # super().__init__(group, target, name, args, kwargs, daemon=daemon)
        Thread.__init__(self) # this is easier
        self.n = n # we could validate with property get/set and mangled names
        self.x = x
    # to behave as a thread we must overwrite the run method
    def run(self):
        '''When this class is invoked the run method is called'''
        for _ in range(0,4):
            print(f'{self.n} is sleeping')
            time.sleep( random.random()*self.x ) # sleep for 0-0.5 sec

if __name__ == '__main__':
    print('on the main thread')
    tA = MyClass('A', 0.5)
    tB = MyClass('B', 0.5)
    tC = MyClass('C', 2)
    start = time.time()
    tA.start()
    tB.start()
    tC.start()
    # we may pause the main thread until the other thrads complete
    tA.join()
    # tB.join()
    # tC.join()


    end = time.time()
    print(f'Total execution: {end-start} sec')

