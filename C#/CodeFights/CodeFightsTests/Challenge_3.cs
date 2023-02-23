/*
 Create simple class that converts roman numerals to integers and vice vers

"IV" = 4
9 = "IX"
etc.

Refer to the unit tests to grasp the idea of this task.
Feel free to add as many unit tests as you want.
No external dependencies!

P.S.: you cant leverage all benefits of classes. ;)
*/

using System.Linq;
using System.Text;

namespace CodeFights
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class Challenge_3
    {
        [Test]
        public void TestToRoman()
        {
            Assert.AreEqual("I", ConvertToRoman(1), "1 should convert to 'I'");
            Assert.AreEqual("II", ConvertToRoman(2), "2 should convert to 'II'");
            Assert.AreEqual("IV", ConvertToRoman(4), "4 should convert to 'IV'");
            Assert.AreEqual("V", ConvertToRoman(5), "5 should convert to 'V'");
            Assert.AreEqual("VI", ConvertToRoman(6), "6 should convert to 'VI'");
            Assert.AreEqual("IX", ConvertToRoman(9), "9 should convert to 'IX'");
            Assert.AreEqual("X", ConvertToRoman(10), "10 should convert to 'X'");
            Assert.AreEqual("XXIII", ConvertToRoman(23), "23 should convert to 'XXIII'");
            Assert.AreEqual("XLIV", ConvertToRoman(44), "44 should convert to 'XLIV'");
            Assert.AreEqual("LIX", ConvertToRoman(59), "59 should convert to 'LIX'");
            Assert.AreEqual("LXXV", ConvertToRoman(75), "75 should convert to 'LXXV'");
            Assert.AreEqual("XCII", ConvertToRoman(92), "92 should convert to 'XCII'");
            Assert.AreEqual("CCLXI", ConvertToRoman(261), "261 should convert to 'CCLXI'");
            Assert.AreEqual("M", ConvertToRoman(1000), "1000 should convert to 'M'");
            Assert.AreEqual("MCDL", ConvertToRoman(1450), "1450 should convert to 'MCDL'");
            Assert.AreEqual("MCMXC", ConvertToRoman(1990), "1990 should convert to 'MCMXC'");
            Assert.AreEqual("MMVIII", ConvertToRoman(2008), "2008 should convert to 'MMVIII'");
            Assert.AreEqual("MMDXXXVII", ConvertToRoman(2537), "2537 should convert to 'MMDXXXVII'");
            Assert.AreEqual("MMMCMXCIX", ConvertToRoman(3999), "3999 should convert to 'MMMCMXCIX'");
        }

        [Test]
        public void TestFromRoman()
        {
            Assert.AreEqual(1, ConvertFromRoman("I"), "'I' should convert to 1");
            Assert.AreEqual(2, ConvertFromRoman("II"), "'II' should convert to 2");
            Assert.AreEqual(4, ConvertFromRoman("IV"), "'IV' should convert to 4");
            Assert.AreEqual(5, ConvertFromRoman("V"), "'V' should convert to 5");
            Assert.AreEqual(6, ConvertFromRoman("VI"), "'VI' should convert to 6");
            Assert.AreEqual(9, ConvertFromRoman("IX"), "'IX' should convert to 9");
            Assert.AreEqual(10, ConvertFromRoman("X"), "'X' should convert to 10");
            Assert.AreEqual(23, ConvertFromRoman("XXIII"), "'XXIII' should convert to 23");
            Assert.AreEqual(44, ConvertFromRoman("XLIV"), "'XLIV' should convert to 44");
            Assert.AreEqual(59, ConvertFromRoman("LIX"), "'LIX' should convert to 59");
            Assert.AreEqual(75, ConvertFromRoman("LXXV"), "'LXXV' should convert to 75");
            Assert.AreEqual(92, ConvertFromRoman("XCII"), "'XCII' should convert to 92");
            Assert.AreEqual(261, ConvertFromRoman("CCLXI"), "'CCLXI' should convert to 261");
            Assert.AreEqual(1000, ConvertFromRoman("M"), "'M' should convert to 1000");
            Assert.AreEqual(1450, ConvertFromRoman("MCDL"), "'MCDL' should convert to 1450");
            Assert.AreEqual(1990, ConvertFromRoman("MCMXC"), "'MCMXC' should convert to 1990");
            Assert.AreEqual(2008, ConvertFromRoman("MMVIII"), "'MMVIII' should convert to 2008");
            Assert.AreEqual(2537, ConvertFromRoman("MMDXXXVII"), "'MMDXXXVII' should convert to 2537");
            Assert.AreEqual(3999, ConvertFromRoman("MMMCMXCIX"), "'MMMCMXCIX' should convert to 3999");
        }

        private static string _placeholderToRoman = "{0} should convert to {1}";
        public static string ConvertToRoman(int n)
        {
            var result = new StringBuilder();
            Enumerable.Range(0, n / 1000).Select(x => x).ToList().ForEach(x => result.Append("M"));
            n = n % 1000;
            n = HandleCase(n, result, 900, "CM");
            n = HandleCase(n, result, 500, "D");
            n = HandleCase(n, result, 400, "CD");
            Enumerable.Range(0, n / 100).Select(x => x).ToList().ForEach(x => result.Append("C"));
            n = n % 100;
            n = HandleCase(n, result, 90, "XC");
            n = HandleCase(n, result, 50, "L");
            n = HandleCase(n, result, 40, "XL");
            Enumerable.Range(0, n / 10).Select(x => x).ToList().ForEach(x => result.Append("X"));
            n = n % 10;
            n = HandleCase(n, result, 9, "IX");
            n = HandleCase(n, result, 5, "V");
            n = HandleCase(n, result, 4, "IV");
            Enumerable.Range(0, n / 1).Select(x => x).ToList().ForEach(x => result.Append("I"));

            return result.ToString();
        }

        private static int HandleCase(int n, StringBuilder result, int limit, string input)
        {
            if (n >= limit)
            {
                result.Append(input);
                n = n - limit;
            }
            return n;
        }

        public static int ConvertFromRoman(string romanNumeral)
        {
            var result = romanNumeral
                .Replace("CM", "A")
                .Replace("CD", "B")
                .Replace("XC", "W")
                .Replace("XL", "Q")
                .Replace("IX", "Y")
                .Replace("IV", "Z");

            int sum = 0;
            foreach (var character in result)
            {
                sum += GetFromChar(character);
            }

            return sum;
        }

        private static int GetFromChar(char c)
        {
            return c switch
            {
                'M' => 1000,
                'D' => 500,
                'C' => 100,
                'L' => 50,
                'X' => 10,
                'V' => 5,
                'I' => 1,
                'A' => 900,
                'B' => 400,
                'W' => 90,
                'Q' => 40,
                'Y' => 9,
                'Z' => 4,
            };
        }
    }
}