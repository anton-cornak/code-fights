import unittest
import time
import timeout_decorator

from challenge_4 import fibonacci_solution


def correct_solution(number: int) -> list[int, bool]:
    """
    Returns Fibonacci product combination
    """
    a, b = 0, 1
    while number > a * b:
        a, b = b, a + b
    return [a, b, number == a * b]


class AlphabetTestCase(unittest.TestCase):
    """
    Unit tests
    """

    @timeout_decorator.timeout(1)
    def test_predefined(self):
        """
        Test
        """
        testcases = [
            714,
            800,
            1870,
            2000,
            4895,
            5895,
            74049690,
            84049690,
            193864606,
            447577,
            602070,
            602070602070,
            256319508074468182850,
            203023208030065646654504166904697594722575,
            203023208030065646654504166904697594722576,
        ]

        for testcase in testcases:
            actual = fibonacci_solution(testcase)
            expected = correct_solution(testcase)
            self.assertEqual(
                actual,
                expected,
                f'\nfailed test case "{testcase}": expected "{expected}", but got "{actual}".',
            )

    @timeout_decorator.timeout(15)
    def test_performance(self):
        """
        Performance test
        """
        times = []

        for _ in range(10):
            st = time.process_time()
            for i in range(100):
                fibonacci_solution(256319508074468182850000**i)
            et = time.process_time()
            times.append(et - st)

        print(
            f"\nYour average execution time is: {sum(times)/len(times)}s.  Benchmark: 1s."
        )


if __name__ == "__main__":
    unittest.main()
