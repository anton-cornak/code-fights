/*
 We all know Fibonacci numbers... If you don't, check good ol' Wikipedia: https://en.wikipedia.org/wiki/Fibonacci_number

Long story short: the Fibonacci sequence

0, 1, 1, 2, 3, 5, 8, 13, 21, 34,...

is calculated as

F(n) = F(n-1) + F(n-2)

However this is going to be a bit more complicated. You are given one number and your task is to find out, whether this number
can be a product of 2 consecutive Fibonacci numbers. If yes, you should return both numbers and True boolean value. Example:

number = 714
result = [21, 34, True]

If not, return 2 Fibonacci numbers, which:

[F(n), F(n+1), false], with F(n) being the smallest one such as F(n) * F(n+1) > given number.

Example:

number = 800
result = [34, 55, False]

because 34 * 55 = 1870 which is more than given number. 

Your code will be tested against huge numbers, so be mindful of performance!

Refer to the unit tests to grasp the idea of this task.
Feel free to add as many unit tests as you want.
No external dependencies!
*/

namespace CodeFights
{
    using NuGet.Frameworks;
    using NUnit.Framework;
    using System;
    using System.Collections.Generic;

    [TestFixture]
    public class Challenge_4
    {
        [Test]
        public void FibonacciTestCase()
        {
            Dictionary<ulong, ulong[]> testCases = new()
            {
                { 4895, new ulong[] { 55, 89, 1 } },
                { 5895,  new ulong[] { 89, 144, 0 } },
                { 74049690, new ulong[] { 6765, 10946, 1 }}
            };

            foreach (var item in testCases)
            {
                Assert.AreEqual(item.Value, FibonacciSolution(item.Key));
            }    
        }        

        public static ulong[] FibonacciSolution(ulong number)
        {
            ulong min = 0;
            ulong max = 1;

            while (min * max < number)
            {
                ulong temp = max;
                max = min + max;
                min = temp;
            }
                
            return new ulong[] { min, max, 
                Multiply(min,max) == number ? (ulong)1 : 0};
        }

        private static ulong Multiply(ulong x, ulong y)
        {
            return x * y;
        }
    }
}