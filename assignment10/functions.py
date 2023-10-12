import math
import unittest

def add_numbers(num1, verbose, num2=math.pi):

  sum = num1 + num2

  sorted_numbers = ([num1, num2])

  if verbose == False:
    return (sum, sorted_numbers)
  if verbose == True:
    return (sum, sorted_numbers, num1, num2)
  

class TestAdd(unittest.TestCase):
    def test_addnumbers(self):
        self.assertEqual(add_numbers(25, True, 25), (50, [25, 25], 25, 25))
        self.assertEqual(add_numbers(653, True, 11), (664, [653, 11], 653, 11))         
        self.assertEqual(add_numbers(100, True, ), (103.141592653589793 , [100, ], 100, ))


if __name__ == '__main__':
  unittest.main()