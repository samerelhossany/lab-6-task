import unittest
from calculator import *
class test_calculator(unittest.TestCase):
  def TestAdd(self):
    self.assertEqual(add(3,7),10)
    self.assertEqual(add(-1,1),0)

if __name__ == '__main__':
    unittest.main()
