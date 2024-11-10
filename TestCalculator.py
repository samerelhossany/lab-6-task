import unittest
from calculator import *
class test_calculator(unittest.TestCase):
  def TestAdd(self):
    self.assertequal(Add(3,7),10)
    self.assertequal(Add(-1,1),0)

if __name__ == '__main__':
    unittest.main()
