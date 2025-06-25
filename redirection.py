import sys

class RedirectOut():
    '''When invoked, this class will redirect the standard output
       to a different output stream.
       When complete, set the standard output back to what it was'''
    def __init__(self, new_stdout):
        self.new_stdout = new_stdout
    # Any method named __enter__ is used every time a class instance is invoked
    def __enter__(self):
        '''swap the standard output to the new standard output'''
        self.orig_stdout = sys.stdout
        sys.stdout = self.new_stdout
    # Any method named __exit__ is used every time a class instance finishes being invoked
    def __exit__(self, exc_type, exc_value, exc_traceback): # we must include these args
        '''put the standard output back to what it was'''
        sys.stdout = self.orig_stdout

if __name__ == '__main__':
    # we may choose to redirect output to a text file
    with open('my_redirect.txt', 'a') as fobj: # 'a' will append. 't' is default
        r = RedirectOut(fobj)
        with r: # each use will invoke __enter__
            print('this will end up in a text file')
        # when the with ends, it will invoke __exit__
    print('normal service is resumed')