from concrete_shape import Shape

class Figure(Shape):
    '''All the properties and methods of 'Shape' are now avauilable inside 'Figure'''
    # we may declare class properties
    count = 0 # this is available to the class (not any particular instance)
    def __init__(self, num_sides, colour='black', id=False):
        # We usually call the __init__ of the super class
        # super().__init__(num_sides, colour) # NB self will automatically be passed
        # alternatively CAREFUL - we must pass 'self'
        Shape.__init__(self, num_sides, colour)
        self.id = id
        Figure.count += 1 # increment the count
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, new_id):
        '''Validate ID to be a positive integer'''
        if type(new_id)==int and new_id >=0:
            self.__id = new_id
        else:
            self.__id = Figure.count # the count belongs to the class (not to any instance)
    def __str__(self):
        s = super().__str__() # this gives us a nice string
        return f'{s} id: {self.id}'
    def howMany(): # this is a class method (not for any particular isntance)
        '''Class methods do NOT take 'self' as an attribute'''
        return Figure.count

if __name__ == '__main__':
    f1 = Figure(4, 'orange') # the ID should be 0
    f2 = Figure(7, 'red')    # the id should be 1
    f3 = Figure(8, 'ochre')  # the id should be 2
    print(f1, f2, f3)
    # we can call methods of hte class itself
    print(f'There are {Figure.howMany()} instances')
