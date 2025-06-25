# this file contains unit tests for our Point class
import unittest
from point import Point

class testPoint(unittest.TestCase):
    '''execute tests against the Point class'''
    # we set up a new Point to be used for each test (no test should depend on other tests)
    def setUp(self):
        self.point = Point(3,4)
    # each test then uses a new Point as declared in setUp
    def testMoveBy(self):
        self.point.moveBy(-5, 2)
        self.assertEqual(self.point.display(), (-2, 6))
    def testMoveBy2(self):
        self.point.moveBy(5, -2)
        self.assertEqual(self.point.display(), (8, 2))
    def testRaises(self): #NB each test must be named 'test....'
        with self.assertRaises(TypeError):
            self.point.moveBy(True, 'oops')

if __name__ == '__main__':
    unittest.main() # this will execute the tests
