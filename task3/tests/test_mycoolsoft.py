import random
import sys
import unittest

from task3.cool_wrapper import _my_cool_soft
from task3.cool_wrapper import count_scores


class TestMyCoolSoft(unittest.TestCase):
    FILE_TO_TEST = ""

    def setUp(self):
        self.my_cool_soft = _my_cool_soft(self.FILE_TO_TEST)

    def test_throws_amount_positive_vals(self):
        """Check that amount of throws is correct"""
        for amount in (0, 1, 10, 100, 1000, 10000, 100000):
            with self.subTest(amount):
                self.assertEqual(len(self.my_cool_soft(amount, 1, 1)), amount, f"Wrong throws result for '{amount}'.")

    def test_throws_amount_negative_vals(self):
        """Check wrong values for amount of throws"""
        for amount in [-1.1, -10000, -1000, -100, -1, 1.1, "a", "."]:
            with self.subTest(amount):
                self.assertEqual(self.my_cool_soft(amount, 1, 1), "Error", f"No error raised for '{amount}' of throws.")

    def test_range_of_dices_positive(self):
        for throws_amount in [1, 10, 50]:
            for dice_range in [(1, 2), (2, 2), (2, 3), (4, 5), (5, 5), (1, 1), (1, 5), (2, 5), (3, 3)]:
                with self.subTest(dice_range):
                    results = self.my_cool_soft(throws_amount, *dice_range)
                    for result in results:
                        self.assertIn(len(result[0]), range(dice_range[0], dice_range[1] + 1))

    def test_amount_of_dices_negative_range(self):
        for dice_range in [(5, 1), (5, 4), (2, 1), (3, 1), (4, 2)]:
            with self.subTest(dice_range):
                result = self.my_cool_soft(1, *dice_range)
                self.assertEqual(result, "Error", "No error thrown for negative range.")

    def test_amount_of_dices_wrong_min_range(self):
        for dice_range in [(-1, 1), (0, 4), (-10, 1), ("a", 2), (1.1, 3), (100, 1)]:
            with self.subTest(dice_range):
                result = self.my_cool_soft(2, *dice_range)
                self.assertEqual(result, "Error", f"No Error thrown for wrong min range '{dice_range}'")

    def test_amount_of_dices_wrong_max_range(self):
        for dice_range in [(1, -1), (4, 0), (1, -4), (2, "a"), (2, 3.1), (2, 10)]:
            with self.subTest(dice_range):
                result = self.my_cool_soft(1, *dice_range)
                self.assertEqual(result, "Error", f"No Error thrown for wrong max range '{dice_range}'")

    def test_wrong_amount_of_3_args(self):
        for dice_range in [("", "", ""), (10, "", ""), (10, 1, ""), (10, "", 1), ("", 1, 3)]:
            with self.subTest(dice_range):
                result = self.my_cool_soft(*dice_range)
                self.assertEqual(result, "Error", f"No error raised for empty values '{str(dice_range)}'")

    def test_scoring_of_results(self):
        for _ in range(200):
            throws = random.randint(1, 10)
            min_d, max_d = 1, random.randint(2, 5)
            results = self.my_cool_soft(throws, min_d, max_d)
            for result in results:
                with self.subTest(result):
                    self.assertEqual(int(result[1]), count_scores(result[0]), f"Wrong score calculation for {result[0]}")

    def test_win_scores(self):
        for result in [
            [(1, 2, 3, 4, 5), 150],
            [(5, 2, 3, 4, 1), 150],
            [(2, 3, 5, 4, 1), 150],
        ]:
            with self.subTest(result):
                self.assertEqual(int(result[1]), count_scores(result[0]), f"Wrong score calculation for {result[0]}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        TestMyCoolSoft.FILE_TO_TEST = sys.argv.pop()
    unittest.main(argv=sys.argv)
