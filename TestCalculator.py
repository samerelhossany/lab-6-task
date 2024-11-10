import unittest
from calculator import *
class test_calculator(unittest.TestCase):
  def TestAdd(self):
    res1=add(3,7)
    res2=add(-1,1)
    self.assertEqual(res1,10)
    self.assertEqual(res2,0)

if __name__ == '__main__':
    unittest.main()
