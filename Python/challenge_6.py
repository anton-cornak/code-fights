"""
You are given a list of ordered numbers. Your task is to extract the range of at least 3 consecutive numbers.

Examples:

numbers = [1, 2, 3, 5, 6, 7, 8, 10]
result = "1-3,5-8,10"

numbers = [-10, -9, -8, -7, -5, -4, -2, 0, 1, 2, 3]
result = "-10--7,-5,-4,-2, 0-3"
etc.

Note how 2 consecutive numbers are not considered a range and therefore are returned separately.

Refer to the unit tests to grasp the idea of this task.
Feel free to add as many unit tests as you want.
No external dependencies!
"""
import unittest


def range_solution(numbers):
    """
    Returns simplified range
    """
    return_list = []

    last_num = numbers[0]
    return_list.append({"min": numbers[0], "max": numbers[0]})
    for num in numbers:
        if num == last_num + 1:
            return_list[len(return_list)-1]["max"] = num
            last_num = num
            continue
        if num >= last_num + 1:
            last_num = num
            return_list.append({"min": num, "max": num})

    ret_str = ""
    for ret in return_list:
        if ret["max"] - ret["min"] >= 2:
            ret_str += "" + str(ret['min']) + "-" + str(ret["max"]) + ","
        else:
            if ret["max"] != ret["min"]:
                ret_str += str(ret["min"]) + "," + str(ret["max"]) + ","
            else:
                ret_str += str(ret["max"]) + ","

    ret_str = ret_str[:len(ret_str)-1]
    return ret_str


class RangeTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test(self):
        """
        Table-driven tests
        """
        testcases = [
            {
                "numbers": [1, 2, 3, 5, 6, 7, 8, 10],
                "res": "1-3,5-8,10",
            },
            {
                "numbers": [-10, -9, -8, -7, -5, -4, -2, 0, 1, 2, 3],
                "res": "-10--7,-5,-4,-2,0-3",
            },
            {
                "numbers": [
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
                "res": "-6,-3-1,3-5,7-11,14,15,17-20",
            },
            {
                "numbers": [-3, -2, -1, 2, 10, 15, 16, 18, 19, 20],
                "res": "-3--1,2,10,15,16,18-20",
            },
        ]

        for case in testcases:
            res = range_solution(case["numbers"])
            self.assertEqual(
                res,
                case["res"],
                f'\nfailed test case "{case["numbers"]}": expected "{case["res"]}", but got "{res}".',
            )


if __name__ == "__main__":
    unittest.main()
