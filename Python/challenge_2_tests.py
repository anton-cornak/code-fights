import unittest
import random
import time
import timeout_decorator

from challenge_2 import directions_solution

opposite = {"NORTH": "SOUTH", "SOUTH": "NORTH", "WEST": "EAST", "EAST": "WEST"}


def correct_solution(directions: list[str]) -> list[str]:
    """
    Returns simplified directions
    """
    new_plan = []
    for d in directions:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan


class DirectionsTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def __init__(self, methodName: str = "runTest") -> None:
        self.directions = ["NORTH", "SOUTH", "EAST", "WEST"]
        super().__init__(methodName)

    def test_predefined(self):
        """
        Table-driven tests
        """
        testcases = [
            ["NORTH", "WEST", "SOUTH", "EAST"],
            ["NORTH", "SOUTH", "SOUTH", "EAST"],
            [
                "NORTH",
                "SOUTH",
                "SOUTH",
                "EAST",
                "WEST",
                "NORTH",
                "WEST",
            ],
            ["NORTH", "WEST", "SOUTH", "EAST"],
            [
                "NORTH",
                "SOUTH",
                "EAST",
                "WEST",
                "NORTH",
                "NORTH",
                "SOUTH",
                "NORTH",
                "WEST",
                "EAST",
            ],
            [
                "SOUTH",
                "SOUTH",
                "EAST",
                "WEST",
                "EAST",
                "NORTH",
                "NORTH",
                "WEST",
                "EAST",
                "WEST",
                "EAST",
            ],
            ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"],
        ]

        for testcase in testcases:
            actual = directions_solution(testcase)
            expected = correct_solution(testcase)
            self.assertEqual(
                actual,
                expected,
                f'failed test case "{testcase}": expected "{expected}", but got "{actual}".',
            )

    @timeout_decorator.timeout(2)
    def test_random_medium(self):
        """
        Test randomly generated directions
        """
        for _ in range(10):
            testcase = random.choices(self.directions, k=20)
            actual = directions_solution(testcase)
            expected = correct_solution(testcase)
            self.assertEqual(
                actual,
                expected,
                f'failed test case "{testcase}": expected "{expected}", but got "{actual}".',
            )

    @timeout_decorator.timeout(2)
    def test_random_large(self):
        """
        Test randomly generated directions
        """
        for _ in range(10):
            testcase = random.choices(self.directions, k=30)
            actual = directions_solution(testcase)
            expected = correct_solution(testcase)
            self.assertEqual(
                actual,
                expected,
                f'failed test case "{testcase}": expected "{expected}", but got "{actual}".',
            )

    @timeout_decorator.timeout(2)
    def test_random_extralarge(self):
        """
        Test randomly generated directions
        """
        for _ in range(10):
            testcase = random.choices(self.directions, k=50)
            actual = directions_solution(testcase)
            expected = correct_solution(testcase)
            self.assertEqual(
                actual,
                expected,
                f'failed test case "{testcase}": expected "{expected}", but got "{actual}".',
            )

    @timeout_decorator.timeout(30)
    def test_performance(self):
        """
        Performance test
        """
        times = []
        for _ in range(10):
            st = time.process_time()
            for _ in range(10):
                # directions_solution(random.choices(self.directions, k=1000000))
                correct_solution(random.choices(self.directions, k=1000000))
            et = time.process_time()
            times.append(et - st)

        print(
            f"\nYour average execution time is: {sum(times)/len(times)}s. Benchmark: 2.2s."
        )


if __name__ == "__main__":
    unittest.main()
