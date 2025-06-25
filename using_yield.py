import datetime
import time
# Python includes a range object. We also met the map and filter objects
# There is also a generator object. They all allow iteration over members

r = range(-4, 35, 3)
g = (i**3 for i in r) # take every member of the collection in r and cube it
print(g.__next__()) # -64
print(g.__next__()) # -1
print('-----------------')
for _ in g:
    print(_)

# if we use [] we do not get a generator, we get a list
l = [i**3 for i in r] # here the gereted values are used to populate a list
print(l)

# we may write our own generator
def makeTS():
    '''yield a timestamp every time we ask for one'''
    while True: # endless loop
        t = datetime.datetime.now().strftime('%H:%M:%S') # we may include day-month-year etc
        yield t # yield instead of return

# sometimes a generator needs limits
def makeSquares(min=0, max=100):
    '''yield the next sqare number between min and max inclusive'''
    value = min
    while True:
        value +=1
        if value > max:
            break # this will end the loop 
        else:
            yield value**2

if __name__ == '__main__':
    # we need an instance of our custom generator
    ts = makeTS()
    print(ts.__next__())
    for _ in range(0,2):
        print(ts.__next__())
        time.sleep(0.5)
    # use the limited generator
    sq =makeSquares(0, 5)
    for _ in sq:
        print(_)
    print(sq.__next__()) # nope - the generator is exhausted

