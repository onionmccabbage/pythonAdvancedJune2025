import sys

# every time we run a python module, sys.argv[0] will be the file name
print(sys.argv, type(sys.argv))

for a in sys.argv: # it is a list
    print(a)