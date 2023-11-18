#!/usr/bin/python3
import unittest
from matrices import *
# --------------------------------------------------------------q4.py
# Two-dimensional arrays, simple algorithms
# --------------------------------------------------------------

# --------------------------------------------------------------
# is there a repeated row?
# --------------------------------------------------------------
def repeatedrow(matrix) :
    '''
    Returns True if an only if at least one row is the same as another row
    False otherwise
    '''
    for x in range(len(matrix)):
        for i in range(x+1, len(matrix)):
            if matrix[x]==matrix[i]:
                return True
    return False
    
# ----------------------------------------------------------
# Show the matrices that we imported 
# matrix1, matrix2 and using printmx()
# --------------------------------------------------------------
printmx(matrix1)
printmx(matrix2)
printmx(matrix3)
printmx(matrix4)
printmx(matrix5)
printmx(matrix6)
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(repeatedrow(matrix1), True)
 def test2(self):
  self.assertEqual(repeatedrow(matrix2), False)
 def test3(self):
  self.assertEqual(repeatedrow(matrix3), False)
 def test4(self):
  self.assertEqual(repeatedrow(matrix4), False)
 def test5(self):
  self.assertEqual(repeatedrow(matrix5), False)
 def test6(self):
  self.assertEqual(repeatedrow(matrix7), True)

if __name__ == '__main__':
 unittest.main(exit=True)


# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
