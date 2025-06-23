# ABC is an Abstract Base Class
from abc import ABCMeta, abstractmethod

class AbstractShape(metaclass=ABCMeta):
    '''Here we declare any methods and properties we wish to be included
    But an abstract class contaons NO implementation code'''
    @abstractmethod # @ is a decorator
    def num_sides(self):
        pass # remember - we write no actual implementaion within abstract class
    @abstractmethod
    def colour(self):
        pass
    @abstractmethod
    def __str__(self):
        '''__str__ will be used if we ever print an instance of the class'''
        pass
