from contextlib import contextmanager
import sys

@contextmanager
def outputRedirect(newOutput):
    '''redirect the sys.stdout'''
    old_stdout = sys.stdout
    sys.stdout = newOutput
    yield # this function will generate a stream of output
    sys.stdout = old_stdout # put back to how things were

if __name__ == '__main__':
    # this is a fancy way to print
    sys.stdout.write('This stream of characters is sent to the usual stdout, i.e. the console')
    with open('my_stream.txt', 'a') as fobj:
        with outputRedirect(fobj):
            print('This will be written to our file')
            sys.stdout.write('...more file content')
    print('back to the console')
    # we don't have to use 'with'
    fobj2 = open('my_stream.txt', 'a')
    with outputRedirect(fobj2):
        print('where does this go')
    fobj2.close()