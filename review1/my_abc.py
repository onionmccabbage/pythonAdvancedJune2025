from abc import ABCMeta, abstractmethod

class ABCReview(metaclass=ABCMeta):
    @property
    @abstractmethod
    def n(self, n):
        pass
    @abstractmethod
    def __str__(self):
        pass