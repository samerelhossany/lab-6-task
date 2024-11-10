import unittest
from calculator import *
class test_calculator(unittest.TestCase):
  def TestAdd(self):
    self.assertequal(add(3,7),10)
    self.assertequal(add(-1,1),0)

if __name__ == '__main__':
    unittest.main()
