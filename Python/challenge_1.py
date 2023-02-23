"""
In the first challange, you are asked to replace every letter with its position in the alphabet.

"a" = 1
"b" = 2
etc.

Return only letters: if string contains other symbols, ignore them.

Refer to the unit tests to grasp the idea of this task.
Feel free to add as many unit tests as you want.
No external dependencies!
"""
import unittest


def alphabet_solution(text: str) -> str:
    """
    Returns letter alphabet position
    """
    res = ""
    for char in text.lower():
        if char.isalpha():
            res += str(ord(char) - 96) + " "
    res = res[:-1]
    return res


class AlphabetTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test(self):
        """
        Table-driven tests
        """
        testcases = [
            {
                "text": "Visma Labs Slovakia",
                "res": "22 9 19 13 1 12 1 2 19 19 12 15 22 1 11 9 1",
            },
            {
                "text": "I love code fights!",
                "res": "9 12 15 22 5 3 15 4 5 6 9 7 8 20 19",
            },
        ]

        for case in testcases:
            res = alphabet_solution(case["text"])
            self.assertEqual(
                res,
                case["res"],
                f'\nfailed test case "{case["text"]}": expected "{case["res"]}", but got "{res}".',
            )


if __name__ == "__main__":
    # alphabet_solution("abcd")
    unittest.main()
