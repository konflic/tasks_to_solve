import unittest

from task1.solution import time_converter

class TestTimeConverter(unittest.TestCase):

    def test_example_one(self):
        self.assertEqual(time_converter("30"), 30)
    
    def test_example_two(self):
        self.assertEqual(time_converter("30s"), 30)

    def test_example_three(self):
        self.assertEqual(time_converter("s"), 1)

    def test_example_four(self):
        self.assertEqual(time_converter("60.5m"), 1)
