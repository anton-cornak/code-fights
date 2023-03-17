import unittest
import random
import time
import timeout_decorator

from challenge_6 import range_solution


def correct_solution(numbers: list[int]) -> str:
    """
    Returns simplified range
    """
    out = []
    strt = end = numbers[0]

    for n in numbers[1:] + [""]:
        if n != end + 1:
            if end == strt:
                out.append(str(strt))
            elif end == strt + 1:
                out.extend([str(strt), str(end)])
            else:
                out.append(str(strt) + "-" + str(end))
            strt = n
        end = n

    return ",".join(out)


class RangeTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test(self):
        """
        Test
        """
        testcases = [
            [1, 2, 3, 5, 6, 7, 8, 10],
            [-10, -9, -8, -7, -5, -4, -2, 0, 1, 2, 3],
            [-3, -2, -1, 2, 10, 15, 16, 18, 19, 20],
            [
                -6,
                -3,
                -2,
                -1,
                0,
                1,
                3,
                4,
                5,
                7,
                8,
                9,
                10,
                11,
                14,
                15,
                17,
                18,
                19,
                20,
            ],
            [
                -61,
                -59,
                -57,
                -55,
                -52,
                -51,
                -48,
                -47,
                -46,
                -43,
                -40,
                -37,
                -35,
                -34,
                -33,
                -32,
                -30,
                -27,
                -26,
                -23,
                -20,
                -19,
                -16,
                -14,
                -13,
            ],
        ]

        for testcase in testcases:
            actual = range_solution(testcase)
            expected = correct_solution(testcase)
            self.assertEqual(
                actual,
                expected,
                f'\nfailed test case "{testcase}": expected "{expected}", but got "{actual}".',
            )

    def test_large(self):
        """
        Test randomly generated strings
        """
        for _ in range(5):
            testcase = sorted(set(random.sample(range(-10, 30), 30)))
            actual = range_solution(testcase)
            expected = correct_solution(testcase)
            self.assertEqual(
                actual,
                expected,
                f'\nfailed test case "{testcase}": expected "{expected}", but got "{actual}".',
            )

    @timeout_decorator.timeout(20)
    def test_performance(self):
        """
        Test randomly generated strings
        """
        times = []

        for _ in range(10):
            st = time.process_time()
            for _ in range(100):
                # range_solution(sorted(set(random.sample(range(-50, 50), 60))))
                correct_solution(
                    sorted(set(random.sample(range(-10000, 10000), 10000)))
                )
            et = time.process_time()
            times.append(et - st)

        print(
            f"\nYour average execution time is: {sum(times)/len(times)}s. Benchmark: 1s."
        )


if __name__ == "__main__":
    unittest.main()
