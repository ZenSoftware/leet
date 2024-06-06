using Leet.LargestNumber;

namespace LeetTests
{
    internal class LargestNumberTest
    {
        [Test]
        public void TestsLargestNumber()
        {
            var solution = new Solution();
            Assert.That(solution.LargestNumber([10, 2]), Is.EqualTo("210"));
            Assert.That(solution.LargestNumber([3, 30, 34, 5, 9]), Is.EqualTo("9534330"));
        }
    }
}
