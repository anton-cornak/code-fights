/*
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
*/

namespace CodeFights
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class Challenge_6
    {
        [Test]
        public void RangeTestCase()
        {
            Assert.AreEqual("1,2", RangeSolution(new[] { 1, 2 }));
            Assert.AreEqual("1-3", RangeSolution(new[] { 1, 2, 3 }));

            Assert.AreEqual(
                "-6,-3-1,3-5,7-11,14,15,17-20",
                RangeSolution(new[] { -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20 })
            );

            Assert.AreEqual(
                "-3--1,2,10,15,16,18-20",
                RangeSolution(new[] { -3, -2, -1, 2, 10, 15, 16, 18, 19, 20 })
            );
        }

        public static string RangeSolution(int[] args)
        {
            /*
             * Returns simplified range
             */
            return String.Empty;
        }
    }
}