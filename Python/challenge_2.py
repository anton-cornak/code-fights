"""
Imagine you are lost in the woods and someone is giving you directions in this form:

["NORTH", "WEST", "SOUTH", "EAST"]

You are getting low on energy and have no potential food in sight.
Naturally, you want to get out of the woods as soon as possible.

But then you remembered elementary school:
If you travel North and then IMMEDIATELY back South, you'll end up exactly where you started.
Same applies to the West/East combination. 

Your task is to simplify directions and remove all consecutive pairs that cancel each other out.
Example: 

["NORTH", "SOUTH", "WEST", "EAST"] is basically just [], right?
["NORTH", "SOUTH", "SOUTH", "EAST"] = ["SOUTH", EAST"]
etc.

Refer to the unit tests to grasp the idea of this task.
Feel free to add as many unit tests as you want.
No external dependencies!

P.S.: don't forget to iterate until you have nothing to remove...
"""
import unittest


def directions_solution(directions: list[str]) -> list[str]:
    """
    Returns simplified directions
    """
    return []


class DirectionsTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test(self):
        """
        Table-driven tests
        """
        testcases = [
            {
                "directions": ["NORTH", "SOUTH", "WEST", "EAST"],
                "res": [],
            },
            {
                "directions": ["NORTH", "SOUTH", "SOUTH", "EAST"],
                "res": ["SOUTH", "EAST"],
            },
            {
                "directions": [
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
                "res": ["NORTH", "NORTH"],
            },
        ]

        for case in testcases:
            res = directions_solution(case["directions"])
            self.assertEqual(
                res,
                case["res"],
                f'failed test case "{case["directions"]}": expected "{case["res"]}", but got "{res}".',
            )


if __name__ == "__main__":
    unittest.main()
