# We will write a class that includes case-blind equality
# e.g. 'hello'=='Hello' # this should be True

class Word():
    'encapsulate a case-blind string'
    def __init__(self, word):
        self.word = word # we could validate this using @property methods
    def __eq__(self, other_word): # we override the built-in __eq__
        '''This __eq__ function will be invoked whenever 
        equality is used for instances of this class'''
        return str(self.word).lower() == str(other_word.word).lower()


if __name__ == '__main__':
    # Normal equality for strings regards case as different
    print('hello'=='Hello') # False
    w1 = Word('Hello')
    w2 = Word('hello')
    print( w1 == w2 ) # True