from collections import namedtuple

# we may need to: python -m pip install pytest

# we will use a named tuple then write test for our code

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


# we invoke pytest like this:
# python -m pytest -v using_nt.py
def testDefaults():
    tA = Task() # a default
    tC = Task(None, None, False, None)
    assert tA == tC

if __name__ == '__main__':
    tDemo = Task() # this will be a default task
    tElse = Task('....', 'Floella', False, 63567)
    print(tDemo, tElse, type(tDemo))