import unittest
from rangeExtraction import solution

class testRangeExtraction(unittest.TestCase):
    """Testing solution function with int arrays of various ranges"""

    def test_large_array(self):
        """testing array of size 20"""
        testVar = solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])
        self.assertEqual(testVar, '-6,-3-1,3-5,7-11,14,15,17-20')

    def test_smaller_array(self):
        """Test solution() with array of smaller length"""
        self.assertEqual(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')


unittest.main()
