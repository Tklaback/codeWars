import unittest
from snail import snail

class TestSnailFunction(unittest.TestCase):
    """Does snail function work with nxn array when n is arbitrary?"""
    
    def test_3_by_3_shell(self):
        """does the function work on a 4 x 4 array?"""
        array = [[1,2,3],
                 [8,9,4],
                 [7,6,5]]
        testVar = snail(array)
        self.assertEqual(testVar, [1,2,3,4,5,6,7,8,9])

    def test_4_by_4_shell(self):
        """Does the function give expected output on a 4 x 4 shell?"""
        array = [[1,2,3,1],
                 [4,5,6,4],
                 [7,8,9,7],
                 [7,8,9,7]]
        testVar = snail(array)
        self.assertEqual(testVar, [1,2,3,1,4,7,7,9,8,7,7,4,5,6,9,8])
    
    def test_5_by_5_shell(self):
        """Does the function give expected output on a 5 x 5 shell?"""
        array = [[1,2,3,4,5],
                 [16,17,18,19,6],
                 [15,24,25,20,7],
                 [14,23,22,21,8],
                 [13,12,11,10,9]]
        testVar = snail(array)
        expected = [num for num in range(1, 26)]
        self.assertEqual(testVar, expected)

unittest.main()
