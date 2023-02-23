"""
Create simple class that converts roman numerals to integers and vice versa.

"IV" = 4
9 = "IX"
etc.

Refer to the unit tests to grasp the idea of this task.
Feel free to add as many unit tests as you want.
No external dependencies!

P.S.: you cant leverage all benefits of classes. ;) 
"""
import unittest


class Convertor:
    """
    Base class that converts roman numerals to integers and vice versa.
    """

    @staticmethod
    def convert_to_roman(integer: int) -> str:
        """
        Integers to roman numerals
        """
        """
                Roman numerals to integers
                """
        # The arabic number to be converted
        t = int(integer)
        # The list contains the number's digits
        l = list()

        # int is not iterable, so I wrote this to get the digits
        while t >= 1:
            l.append(int(t % 10))
            t = t / 10

        # They are in the wrong order, so the list has to be reversed
        l.reverse()

        # The format
        format = ""

        # Current position in the number
        c = 0

        # If the number is at least 1000
        if len(l) >= 4:
            num = 0

        # All the digits after 1000
        i = int(len(l) - 1)
        while i > 3:
            num = num + 1
            i = i - 1

            # A list containing these digits
        li = list()

        for i in range(0, num + 1):
            li.append(l[i])

        # Converts the list to an int
        n = map(str, li)
        n = ''.join(n)
        n = int(n)

        # Add an 'M' for every 1000
        for i in range(0, n):
            format = format + 'M'

        c = num + 1

        # If the number is also least 100
        if len(l) >= 3:
            format = format + encode(l, c, 'C', 'D', "CM")
            c = c + 1

        # If the number is at least 10
        if len(l) >= 3:
            format = format + encode(l, c, 'X', 'L', "XC")
            c = c + 1

        # If the number is at least 100 but smaller than 1000
        if len(l) > 2:
            format = format + encode(l, c, 'I', 'V', "IX")

        # If the number is at least 10 but smaller than 100
        if len(l) == 2:
            format = format + encode(l, c, 'X', 'L', "XC")
            c = c + 1
            format = format + encode(l, c, 'I', 'V', "IX")

        # If the number is at least 1 but smaller than 10
        if len(l) == 1:
            format = format + encode(l, c, 'I', 'V', "IX")

        return format
        return ""

    @staticmethod
    def convert_to_integers(roman):
        # Hold the numbers in the list
        l = list()

        # The format
        format = 0

        # Convert from roman numeral to arabic number
        for i in range(0, len(roman)):
            if roman[i] == 'I':
                l.append(int(1))
            elif roman[i] == 'V':
                l.append(int(5))
            elif roman[i] == 'X':
                l.append(int(10))
            elif roman[i] == 'L':
                l.append(int(50))
            elif roman[i] == 'C':
                l.append(int(100))
            elif roman[i] == 'D':
                l.append(int(500))
            elif roman[i] == 'M':
                l.append(int(1000))

        # Calculate the format as follows:
        i = 0
        while i < len(l) - 1:
            # If the next numeral is greater than the current one, add the next one minus the current one = format = format + next_numeral - current_numeral
            if l[i] < l[i + 1]:
                format = format + l[i + 1] - l[i];
                i = i + 2
            # Else add it normally
            else:
                format = format + l[i]
                i = i + 1

        # Fix in case the last two numerals are equal
        if i == len(l):
            if l[i - 2] == l[i - 1]:
                format = format + l[i - 1]
        else:
            format = format + l[i]

        # Return the format
        return format


def encode(l, c, one, five, nine):
    # The format to be returned
    format = ""

    # Special case 5.1: 5 has its own numeral 'V'
    # Special case 5.2: 50 has its own numeral 'A'
    # Special case 5.3: 500 has its own numeral 'D'
    if l[c] == 5:
        format = format + five
    elif l[c] < 5:
        for i in range(0, l[c]):
            format = format + one
    elif l[c] > 5:
        # Special case 9.1: 9 depends on 10, so it's 'IX'
        # Special case 9.2: 90 depends on 1000, so it's 'XC'
        # Special case 9.3: 900 depends on 1000, so it's 'CM'
        if l[c] == 9:
            format = format + nine
        else:
            format = format + five
            for i in range(6, l[c] + 1):
                format = format + one

    return format


class ConvertorTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def __init__(self, methodName: str = "runTest") -> None:
        """
        Superconstructor
        """
        self.convertor = Convertor()
        self.test_cases = [
            {
                "integer": 1995,
                "roman": "MCMXCV",
            },
            {
                "integer": 2023,
                "roman": "MMXXIII",
            },
        ]
        super().__init__(methodName)

    def test_convert_to_roman(self):
        """
        Table-driven tests
        """
        for case in self.test_cases:
            res = self.convertor.convert_to_roman(case["integer"])
            self.assertEqual(
                res,
                case["roman"],
                f'\nfailed test case "{case["integer"]}": expected "{case["roman"]}", but got "{res}".',
            )

    def test_convert_to_integers(self):
        """
        Table-driven tests
        """
        for case in self.test_cases:
            res = self.convertor.convert_to_integers(case["roman"])
            self.assertEqual(
                res,
                case["integer"],
                f'\nfailed test case "{case["roman"]}": expected "{case["integer"]}", but got "{res}".',
            )


if __name__ == "__main__":
    unittest.main()
