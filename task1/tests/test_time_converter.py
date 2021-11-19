import unittest

from task1.solution import time_converter


class TestTimeConverter(unittest.TestCase):

    def test_positive_cases(self):
        testcases = (
            ("30", 30),
            ("30s", 30),
            ("2h", 60 * 60 * 2),
            ("10m", 60 * 10),
            ("s", 1),
            ("m", 60),
            ("h", 60 * 60),
            ("d", 60 * 60 * 24),
            ("60.5m", 3630),
            ("100h", 60 * 60 * 100)
        )

        for testcase in testcases:
            with self.subTest(testcase):
                self.assertEqual(time_converter(testcase[0]), testcase[1])

    def test_negative_cases(self):
        testcases = ("", "10seconds", "1y", "1m30s", "30ss", "10s30ss")

        for testcase in testcases:
            with self.subTest(testcase):
                self.assertRaises(ValueError, time_converter, testcase)

