
class Point():
    '''define a pont in 2d space using x and y validated as numeric
    we will derive the hypotenuse from x and y
    A 'move' method allow the point to be changed by dx and dy '''
    def __init__(self, x ,y):
        self.x = x
        self.y = y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, new_x):
        if type(new_x) in (int, float):
            self.__x = new_x
        else:
            raise TypeError('X must be a number')
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, new_y):
        if type(new_y) in (int, float):
            self.__y = new_y
        else:
            raise TypeError('Y must be a number')
    def moveBy(self, dx, dy):
        '''move the point by dx and dy'''
        if type(dx) in (int, float) and type(dy) in (int, float):
            self.x += dx
            self.y += dy
        else:
            raise TypeError('Cannot move by non-numeric value')
    def hypot(self):
        return (self.x**2+self.y**2)**0.5
    def display(self):
        return (self.x, self.y) # useful in tests
    
if __name__ == '__main__':
    p1 = Point(3,4)
    print(p1.x, p1.y, p1.hypot())
    