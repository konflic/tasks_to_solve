import unittest

from task1.solution import time_converter


class TestTimeConverter(unittest.TestCase):

    def test_empty_string(self):
        self.assertRaises(ValueError, time_converter, "")

    def test_long_word(self):
        self.assertRaises(ValueError, time_converter, "10seconds")

    def test_wrong_letter(self):
        self.assertRaises(ValueError, time_converter, "1y")

    def test_wrong_mix_of_letters(self):
        self.assertRaises(ValueError, time_converter, "1m30s")

    def test_wrong_double_letter(self):
        self.assertRaises(ValueError, time_converter, "30ss")
