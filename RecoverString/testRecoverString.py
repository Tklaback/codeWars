import unittest
from recoverString import recoverSecret

class TestRecoverString(unittest.TestCase):
    """Test recoverSecret function with various random triplets"""

    def test_7_by_3_triplets(self):
        """Does the function pass when given a 7 x 3 list of lists?"""
        secret = "whatisup"
        triplets = [
            ['t','u','p'],
            ['w','h','i'],
            ['t','s','u'],
            ['h','a','p'],
            ['t','i','s'],
            ['w','h','s'],
            ['a','t','s']
        ]
        self.assertEqual(recoverSecret(triplets), secret)
    
    def test_10_by_3_triplets(self):
        """Does the function work on a 10 by 3 list of lists?"""
        secret = "solved"
        triplets = [
            ['l','e','d'],
            ['o','e','d'],
            ['o','l','e'],
            ['o','v','e'],
            ['s','o','l'],
            ['s','e','d'],
            ['s','l','e'],
            ['v','e','d'],
            ['o','l','v'],
            ['l','v','d']
        ]
        self.assertEqual(recoverSecret(triplets), secret)

    def test_17_by_3_triplets(self):
        """Does the function work on a 17 x 13 list of lists?"""
        secret = "mathisfun"
        triplets = [
            ['t','s','f'],
            ['a','s','u'],
            ['m','a','f'],
            ['a','i','n'],
            ['s','u','n'],
            ['m','f','u'],
            ['a','t','h'],
            ['t','h','i'],
            ['h','i','f'],
            ['m','h','f'],
            ['a','u','n'],
            ['m','a','t'],
            ['f','u','n'],
            ['h','s','n'],
            ['a','i','s'],
            ['m','s','n'],
            ['m','s','u']
        ]
        self.assertEqual(recoverSecret(triplets), secret)

unittest.main()