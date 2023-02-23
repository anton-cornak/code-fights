"""
You are given a positive ingeter. Your task is to return multiplicative persistence: https://en.wikipedia.org/wiki/Persistence_of_a_number.

Long story short: number of times you need to multiply the digits in a given number until you reach a single digit. Examples:

num = 10 
res = 1
explanation: 1•0 = 0, which is a single digit number

num = 963
res = 3
explanation: 9*6*3 = 162 -> 1*6*2 = 12 -> 1*2 = 2, which is a single digit number

Refer to the unit tests to grasp the idea of this task.
Feel free to add as many unit tests as you want.
No external dependencies!
"""
import unittest


def persistence_solution(number: int) -> int:
    """
    Returns persistence of a number
    """
    count = 0

    return recursive_multiplication(number, count)

def recursive_multiplication(number, count):
    if number < 10:
        return count
    list_of_numbers = [int(d) for d in str(number)]
    multiplication = 1
    if 0 in list_of_numbers:
        return count+1
    for num in list_of_numbers:
        multiplication *= num
    count += 1
    return recursive_multiplication(multiplication, count)

class PersistenceTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test(self):
        testcases = [
            {
                "number": 5,
                "res": 0,
            },
            {
                "number": 999,
                "res": 4,
            },
            {
                "number": 10,
                "res": 1,
            },
            {
                "number": 10000000,
                "res": 1,
            },
            {
                "number": 143856743785642387568462573427547832,
                "res": 2,
            }
        ]
        """
        Table-driven tests
        """

        for case in testcases:
            res = persistence_solution(case["number"])
            self.assertEqual(
                res,
                case["res"],
                f'\nfailed test case "{case["number"]}": expected "{case["res"]}", but got "{res}".',
            )


if __name__ == "__main__":
    unittest.main()
