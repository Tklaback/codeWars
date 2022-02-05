import unittest
from sumOfIntervals import sum_of_intervals

class SumTestCase(unittest.TestCase):

    def test_no_intervals(self):
        """Does passing the function no parameters return 0?"""
        testVar = sum_of_intervals([])
        self.assertEqual(testVar, 0)
    
    def test_one_interval(self):
        """Does the test act as expected with one parameter?"""
        testVar = sum_of_intervals([(1, 5)])
        self.assertEqual(testVar, 4)

    def test_overlapping_intervals(self):
        testVar = sum_of_intervals([(1, 4), (7, 10), (3, 5)])
        self.assertEqual(testVar,7)

    def test_large_intervals(self):
        testVar = sum_of_intervals([(9, 13), (7, 10), (6, 7), (21, 45), (17, 29)])
        self.assertEqual(testVar, 35)

unittest.main()
