using Leet.HouseRobber;

namespace LeetTests
{
    internal class HouseRobberTest
    {
        [Test]
        public void TestsHouseRobber()
        {
            var solution = new Solution();
            Assert.That(
                solution.Rob([1, 2, 3, 1]),
                Is.EqualTo(4)
            );
            Assert.That(
                solution.Rob([2, 7, 9, 3, 1]),
                Is.EqualTo(12)
            );
            Assert.That(
                solution.Rob([2, 1, 1, 2]),
                Is.EqualTo(4)
            );
        }
    }
}
