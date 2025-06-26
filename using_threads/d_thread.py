import threading # or from threading import Thread
import time
import timeit # really good at measuring only the time taken by Python (ignore OS)
import random

testsAvailable = [] # this will end up containing 100 tests dict items
# careful - the OS will limit how many concurrent threads we may use
numthreads     = 1024 # we may vary how many threads we choose to use

# we often need to balance the number of threads with the number of things that need doing
for _ in range(0,4098): 
    t = {'id':_, 'kind':'Python'}
    testsAvailable.append(t)

class TestRunner(threading.Thread):
    '''Each instasnce will be executed on a separate thread
    to run one of a finite collection of tests'''
    tests_completed = 0 # this belongs to the class (not to any aprticular isntance)
    def __init__(self, lock):
        threading.Thread.__init__(self)
        self.lock = lock
        self.test_count = 0
    def run(self):
        global testsAvailable
        running = True
        while running:
            self.randomDelay() # emulate an unpredictable amount of time
            self.lock.acquire()
            if len(testsAvailable)>0:
                whichTest = testsAvailable.pop() # removes the end-most member
                # we would do things with the whichTest object
                self.test_count += 1
            else: # if there are no more tests
                running = False
            self.lock.release()
        # print(f'Ran {self.test_count}')
    def randomDelay(self):
        time.sleep(random.randint(0,4)/4) # 0, 0.25, 0.5, 1.0

if __name__ == '__main__':
    lock = threading.Lock() # one instance of a lock
    # here is a method to manage many threads
    runners_l = []
    for _ in range(0, numthreads):
        runner = TestRunner(lock)
        runners_l.append(runner)
    s = timeit.default_timer()
    for _ in runners_l:
        _.start()
    for _ in runners_l:
        _.join()
    e = timeit.default_timer()
    print(f'total {e-s} sec')

