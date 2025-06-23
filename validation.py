# we can use several features to check the kind of data we are dealing with

# using isinstance
t = (2,3,4,5)
l = ['68756','-654655','90854','2546.3456']
if isinstance(t, tuple):
    print(f'{t} is a tuple')

for _ in l:
    # isnumeric can ONLY be used on strings
    # returns True if the string contains nothing but digits
    print( _.isnumeric() )
    print( _.isdecimal() )
    print( _.isdigit() )
    print('----------------------')