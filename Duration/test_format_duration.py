import unittest
from formatDuration import format_duration

class TestFormatDuration(unittest.TestCase):
    """Testing the format_duration function"""

    def test_seconds(self):
        """Does format_duration work when I pass it seconds under a minute?"""
        self.assertEqual(format_duration(25), "25 seconds")
    
    def test_at_60_seconds(self):
        """Does 60 seconds display 1 minute and not 60 seconds?"""
        self.assertEqual(format_duration(60), "1 minute")
    
    def test_more_than_a_minute(self):
        """Does the function return the correct output if seconds are well over 1 minute?"""
        self.assertEqual(format_duration(121), "2 minutes and 1 second")
    
    def test_hours(self):
        """Does the function perform regularly if seconds are more than an hour?"""
        self.assertEqual(format_duration(3662), "1 hour, 1 minute and 2 seconds")

    def test_days(self):
        """Does the function display the proper days along with hours minutes and seconds?"""
        self.assertEqual(format_duration(15731080), "182 days, 1 hour, 44 minutes and 40 seconds")

    def test_years(self):
        """Does function display the proper years?"""
        self.assertEqual(format_duration(132030240), "4 years, 68 days, 3 hours and 4 minutes")
        self.assertEqual(format_duration(205851834), "6 years, 192 days, 13 hours, 3 minutes and 54 seconds")
        self.assertEqual(format_duration(253374061), "8 years, 12 days, 13 hours, 41 minutes and 1 second")
        self.assertEqual(format_duration(242062374), "7 years, 246 days, 15 hours, 32 minutes and 54 seconds")
        self.assertEqual(format_duration(101956166), "3 years, 85 days, 1 hour, 9 minutes and 26 seconds")
        self.assertEqual(format_duration(33243586), "1 year, 19 days, 18 hours, 19 minutes and 46 seconds")

unittest.main()