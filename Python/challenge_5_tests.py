import unittest
import random
import time
import timeout_decorator

from challenge_5 import persistence_solution


def correct_solution(number: int) -> int:
    """
    Returns persistence of a number
    """
    n = str(number)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count


class PersistenceTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test(self):
        """
        Test
        """
        testcases = [39, 4, 25, 999, 100, 444]

        for testcase in testcases:
            actual = persistence_solution(testcase)
            expected = correct_solution(testcase)
            self.assertEqual(
                actual,
                expected,
                f'\nfailed test case "{testcase}": expected "{expected}", but got "{actual}".',
            )

    @timeout_decorator.timeout(2)
    def test_large(self):
        """
        Test randomly generated strings
        """
        for _ in range(30):
            testcase = random.randint(1000, 100000)
            actual = persistence_solution(testcase)
            expected = correct_solution(testcase)
            self.assertEqual(
                actual,
                expected,
                f'\nfailed test case "{testcase}": expected "{expected}", but got "{actual}".',
            )

    @timeout_decorator.timeout(20)
    def test_performance(self):
        """
        Performance test
        """
        times = []

        for _ in range(20):
            st = time.process_time()
            for _ in range(100):
                persistence_solution(random.randint(10**10000, 10**11000))
            et = time.process_time()
            times.append(et - st)

        print(
            f"\nYour average execution time is: {sum(times)/len(times)}s. Benchmark: 0.3s."
        )


if __name__ == "__main__":
    unittest.main()
