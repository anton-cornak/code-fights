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
from typing import List


def directions_solution(directions: List[str]) -> List[str]:
    """
    Returns simplified directions
    """
    out = []
    n,s,e,w = 0,0,0,0
    for direction in directions:
        if direction == "NORTH":
            n += 1
            s -= 1
        elif direction == "SOUTH":
            s += 1
            n -= 1
        elif direction == "EAST":
            e += 1
            w -= 1
        elif direction == "WEST":
            w += 1
            e -= 1
    while n > 0:
        out.append("NORTH")
        n -= 1
    while s > 0:
        out.append("SOUTH")
        s -= 1
    while e > 0:
        out.append("EAST")
        e -= 1
    while w > 0:
        out.append("WEST")
        w -= 1
    return out


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
