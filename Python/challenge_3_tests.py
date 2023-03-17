import unittest
import random
from collections import OrderedDict

from challenge_3 import Convertor


class CorrectConvertor:
    """
    Base class that converts roman numerals to integers and vice versa.
    """

    @staticmethod
    def convert_to_roman(integer: int) -> str:
        """
        Integers to roman numerals
        """
        conversions = OrderedDict(
            [
                ("M", 1000),
                ("CM", 900),
                ("D", 500),
                ("CD", 400),
                ("C", 100),
                ("XC", 90),
                ("L", 50),
                ("XL", 40),
                ("X", 10),
                ("IX", 9),
                ("V", 5),
                ("IV", 4),
                ("I", 1),
            ]
        )
        out = ""
        for key, value in conversions.items():
            while integer >= value:
                out += key
                integer -= value
        return out

    @staticmethod
    def convert_to_integers(roman: str) -> int:
        """
        Roman numerals to integers
        """
        conversions = OrderedDict(
            [
                ("CM", 900),
                ("CD", 400),
                ("XC", 90),
                ("XL", 40),
                ("IX", 9),
                ("IV", 4),
                ("M", 1000),
                ("D", 500),
                ("C", 100),
                ("L", 50),
                ("X", 10),
                ("V", 5),
                ("I", 1),
            ]
        )
        out = 0
        for key, value in conversions.items():
            out += value * roman.count(key)
            roman = roman.replace(key, "")
        return out


class ConvertorTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def __init__(self, methodName: str = "runTest") -> None:
        self.convertor = Convertor()
        self.correct_solution = CorrectConvertor()
        super().__init__(methodName)

    def test_convert_to_roman(self):
        """
        Test
        """
        testcases = [1, 4, 9, 14, 19, 90, 400, 900, 3999]

        for testcase in testcases:
            actual = self.convertor.convert_to_roman(testcase)
            expected = self.correct_solution.convert_to_roman(testcase)
            self.assertEqual(
                actual,
                expected,
                f'\nfailed test case "{testcase}": expected "{expected}", but got "{actual}".',
            )

    def test_convert_to_integers(self):
        """
        Test
        """

        testcases = ["I", "IV", "IX", "XIX", "XC", "CD", "CM", "MMMCMXCIX"]
        for testcase in testcases:
            actual = self.convertor.convert_to_integers(testcase)
            expected = self.correct_solution.convert_to_integers(testcase)
            self.assertEqual(
                actual,
                expected,
                f'\nfailed test case "{testcase}": expected "{expected}", but got "{actual}".',
            )

    def test_convert_to_integers_random(self):
        """
        Test
        """
        for _ in range(100):
            testcase = random.randint(1, 3999)
            actual = self.convertor.convert_to_roman(testcase)
            expected = self.correct_solution.convert_to_roman(testcase)
            self.assertEqual(
                actual,
                expected,
                f'\nfailed test case "{testcase}": expected "{expected}", but got "{actual}".',
            )

    def test_convert_to_roman_random(self):
        """
        Test
        """
        for _ in range(100):
            testcase_integer = random.randint(1, 3999)
            testcase = self.correct_solution.convert_to_roman(testcase_integer)
            actual = self.convertor.convert_to_integers(testcase)
            self.assertEqual(
                actual,
                testcase_integer,
                f'\nfailed test case "{testcase}": expected "{testcase_integer}", but got "{actual}".',
            )


if __name__ == "__main__":
    unittest.main()
