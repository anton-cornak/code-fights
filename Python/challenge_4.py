"""
We all know Fibonacci numbers... If you don't, check good ol' Wikipedia: https://en.wikipedia.org/wiki/Fibonacci_number

Long story short: the Fibonacci sequence

0, 1, 1, 2, 3, 5, 8, 13, 21, 34,...

is calculated as

F(n) = F(n-1) + F(n-2)

However this is going to be a bit more complicated. You are given one number and your task is to find out, whether this number
can be a product of 2 consecutive Fibonacci numbers. If yes, you should return both numbers and True boolean value. Example:

number = 714
result = [21, 34, True]

If not, return 2 Fibonacci numbers, which:

[F(n), F(n+1), false], with F(n) being the smallest one such as F(n) * F(n+1) > given number.

Example:

number = 800
result = [34, 55, False]

because 34 * 55 = 1870 which is more than given number. 

Your code will be tested against huge numbers, so be mindful of performance!

Refer to the unit tests to grasp the idea of this task.
Feel free to add as many unit tests as you want.
No external dependencies!
"""
import unittest
from typing import List


def fibonacci_solution(number: int) -> List[int, bool]:

    """
    Returns Fibonacci product combination
    """

    return [0, 1, False]


class FibonacciTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test(self):
        """
        Table-driven tests
        """
        testcases = [
            {
                "number": 714,
                "res": [21, 34, True],
            },
            {
                "number": 800,
                "res": [34, 55, False],
            },
            {
                "number": 1870,
                "res": [34, 55, True],
            },
            {
                "number": 2000,
                "res": [55, 89, False],
            },
        ]

        for case in testcases:
            res = fibonacci_solution(case["number"])
            self.assertEqual(
                res,
                case["res"],
                f'\nfailed test case "{case["number"]}": expected "{case["res"]}", but got "{res}".',
            )


if __name__ == "__main__":
    unittest.main()
