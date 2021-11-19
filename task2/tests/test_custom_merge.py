import unittest
import heapq

from task2.solution import my_merge, generate_iterables


class TestCustomMergeImplementation(unittest.TestCase):
    """Testing against reference implementation of heapq.merge"""

    def test_control_of_failures(self):
        self.assertNotEqual(
            list(my_merge(*[iter(l) for l in ([1, 5], [2, 5], [1, 10, 11])])),
            list(heapq.merge(*[iter(l) for l in ([1, 5], [2, 5], [1, 6, 10, 11])]))
        )

    def test_realization(self):
        testcases = (
            ([1, 5, 9], [2, 5], [1, 6, 10, 11]),
            ([1, 5, 9, 100], [4, 5, 6, 200, 500, 1000], [7, 8, 11, 400, 1002, 1003]),
            ([1, 5, 9, 100], []),
            ([], [], []),
            ([1, 2, 3], [], []),
            ([1, 100, 101], [10, 200, 300, 399, 10000], [20, 400, 1000]),
            ([-2, 100], [1, 2, 3], [1, 4], [1, 2, 9, 10], [1, 100], [2, 3, 101, 102], [-1, 1])
        )

        for testcase in testcases:
            with self.subTest(testcase=testcase):
                it1, it2 = generate_iterables(*testcase)

                self.assertEqual(
                    list(my_merge(*it1)),
                    list(heapq.merge(*it2))
                )
