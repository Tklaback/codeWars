import unittest
from josephusPermutation import josephus

class TestJosephus(unittest.TestCase):
    """Tests for the function Josephus"""

    def test_10_elements(self):
        """tests array of 10 elements, removing every 2nd element"""
        returnVar = josephus([1,2,3,4,5,6,7,8,9,10],2)
        self.assertEqual(returnVar, [2, 4, 6, 8, 10, 3, 7, 1, 9, 5])
    
    def test_string_array(self):
        """will this work on a string array?"""
        returnVar = josephus(["C","o","d","e","W","a","r","s"],4)
        self.assertEqual(returnVar, ['e', 's', 'W', 'o', 'C', 'd', 'r', 'a'])
    
    def test_every_40th_element(self):
        """Will it work with big numbers as the step?"""
        returnVar = josephus([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],40)
        self.assertEqual(returnVar, [10, 7, 8, 13, 5, 4, 12, 11, 3, 15, 14, 9, 1, 6, 2])
    
    def test_empty_array(self):
        """Will it work on an empty array?"""
        returnVar = josephus([],3)
        self.assertEqual(returnVar, [])

unittest.main()
