// #define false true
/*
Create variable, that is both True and False. ;)

Be creative, there are multiple correct answers. But you can't make any changes in unit tests!!! Not even rename the variable.
*/

namespace CodeFights
{
    using NUnit.Framework;
    using System;



    [TestFixture]
    public class Challenge_Bonus
    {        
        [Test]
        public void SchroedingerTestCase()
        {
            /*
             * Should pass!
             */
            bool SCHROEDINGER = false;
            Assert.IsTrue(SCHROEDINGER == true && SCHROEDINGER == false);

        }
    }
}