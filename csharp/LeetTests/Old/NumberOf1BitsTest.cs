using Old.NumberOf1Bits;

namespace LeetTests.Old
{
    internal class NumberOf1BitsTestTest
    {
        [Test]
        public void TestsNumberOf1BitsTest()
        {
            var solution = new Solution();
            Assert.That(
                solution.HammingWeight(11),
                Is.EqualTo(3)
            );
            Assert.That(
                solution.HammingWeight(128),
                Is.EqualTo(1)
            );
            Assert.That(
                solution.HammingWeight(2147483645),
                Is.EqualTo(30)
            );
        }
    }
}
