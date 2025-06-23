

class Shape:
    def __init__(self, num_sides):
        '''very time we make an instance the __init__ is called'''
        self.num_sides = num_sides # this will call the setter function
    @property # this is a decorator: it adds functionality
    def num_sides(self): # this is the getter for num_sides
        # we use __ to mangle the proerty name within a class.
        # This makes it very hard to access from outside the class
        return self.__num_sides
    @num_sides.setter # this is the setter for num_sides
    def num_sides(self, new_num_sides):
        '''we can validate the num_sides to be a positive integer'''
        if type(new_num_sides)==int and new_num_sides > 0:
            self.__num_sides = new_num_sides
        else:
            raise TypeError('Number of sides must be a positive integer')

if __name__ == '__main__':
    '''here we can exercise the code within this module'''
    # we need instances of our class
    s1 = Shape(3)
    # currently there is no valiation of the class properties
    # s2 = Shape('many') # this will raise a TypeError

    # print(s1.__num_sides) # this will fail
    print(s1.num_sides)