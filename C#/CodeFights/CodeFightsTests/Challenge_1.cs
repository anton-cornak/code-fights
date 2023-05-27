/*
 * In the first challange, you are asked to replace every letter with its position in the alphabet.

"a" = 1
"b" = 2
etc.

Return only letters: if string contains other symbols, ignore them.

Refer to the unit tests to grasp the idea of this task.
Feel free to add as many unit tests as you want.
No external dependencies!
*/

using System.Linq;

namespace CodeFights
{
    using NUnit.Framework;
    using System;
    using System.Collections.Generic;

    [TestFixture]
    public class Challenge_1
    {
        static string alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            
        public static string AlphabetSolution(string text)
        {
            text = text.Replace(" ", "").Replace("!", "");

            var parsed = Enumerable
                .Range(0, text.Length)
                .Select(index => GetChar(text, index));
            
            return string.Join(" ", parsed);
        }

        private static int GetChar(string text, int index)
        {
            return alpha.IndexOf(text[index].ToString().ToUpperInvariant()) + 1;
        }

        [Test]
        public void AlphabetTest()
        {
            Dictionary<string, string> testCases = new()
            {
                { "Visma Labs Slovakia", "22 9 19 13 1 12 1 2 19 19 12 15 22 1 11 9 1" },
                { "I love code fights!", "9 12 15 22 5 3 15 4 5 6 9 7 8 20 19" }
            };

            foreach (var testCase in testCases)
            {
                string expected = AlphabetSolution(testCase.Key);
                Assert.AreEqual(expected, testCase.Value);
            }
        }
    }
}