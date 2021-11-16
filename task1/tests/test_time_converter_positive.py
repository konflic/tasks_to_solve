import unittest

from task1.solution import time_converter


class TestTimeConverter(unittest.TestCase):

    def test_example_one(self):
        self.assertEqual(time_converter("30"), 30)

    def test_example_num_with_sec(self):
        self.assertEqual(time_converter("30s"), 30)

    def test_example_num_with_hrs(self):
        self.assertEqual(time_converter("2h"), 60 * 60 * 2)

    def test_example_num_with_min(self):
        self.assertEqual(time_converter("10m"), 60 * 10)

    def test_example_second_str(self):
        self.assertEqual(time_converter("s"), 1)

    def test_example_minute_str(self):
        self.assertEqual(time_converter("m"), 60)

    def test_example_hour_str(self):
        self.assertEqual(time_converter("h"), 60 * 60)

    def test_example_day_str(self):
        self.assertEqual(time_converter("d"), 60 * 60 * 24)

    def test_example_float_with_letter(self):
        self.assertEqual(time_converter("60.5m"), 3630)
