/*
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
*/

using System.Linq;

namespace CodeFights
{
    using NUnit.Framework;
    using System;
    using System.Collections.Generic;

    [TestFixture]
    public class Challenge_2
    {
        [Test]
        public void Test1()
        {
            string[] a = new string[] { "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
            string[] b = new string[] { "WEST" };
            

            Dictionary<string[], string[]> testCases = new()
            {
                { new string[] { "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" },  new string[] { "WEST" }},
                { new string[] { "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH" }, new string[] { "NORTH" }}
            };

            foreach (var item in testCases)
            {
                Assert.AreEqual(item.Value, DirectionsSolution(item.Key));
            }
        } 

        public static String[] DirectionsSolution(String[] arr)
        {
            var westEast = arr.Select(x => x == "WEST" ? 1 : (x == "EAST" ? -1 : 0));
            var westEastResult = Enumerable.Sum(westEast);
            
            var northSouth = arr.Select(x => x == "NORTH" ? 1 : (x == "SOUTH" ? -1 : 0));
            var northSouthResult = Enumerable.Sum(northSouth);

            var result = new List<string>();
            if (northSouthResult != 0)
            {
                result.Add(northSouthResult > 0 ? "NORTH" : "WEST");
            }
            if (westEastResult != 0)
            {
                result.Add(westEastResult > 0 ? "WEST" : "EAST");
            }

            return result.ToArray();
        }
    }
}