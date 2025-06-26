from threading import Thread
from threading import Lock

count = 0 # this could be a shared resource, maybe a DB, a file, an API, a service....
# we may provide a lock
lock = Lock()

# we do not want threads arguing over shared resources
def fnA():
    '''increment count to 100'''
    global count
    lock.acquire()
    while count <100:
        count += 1
        print(f'A increments count to {count}')
    lock.release()

def fnB():
    '''decrement count to -100'''
    global count
    # global lock # lock is designed to act globally when required
    lock.acquire()
    while count >-100:
        count -= 1
        print(f'B decrements count to {count}')
    lock.release()

if __name__ == '__main__':
    tA = Thread(target=fnA)
    tB = Thread(target=fnB)
    tA.start()
    tB.start()
    tA.join()
    tB.join()