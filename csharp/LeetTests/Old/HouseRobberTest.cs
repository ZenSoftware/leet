using Old.HouseRobber;

namespace LeetTests.Old
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
            Assert.That(
                solution.Rob([1, 2, 1, 1]),
                Is.EqualTo(3)
            );
            Assert.That(
                solution.Rob([104, 209, 137, 52, 158, 67, 213, 86, 141, 110, 151, 127, 238, 147, 169, 138, 240, 185, 246, 225, 147, 203, 83, 83, 131, 227, 54, 78, 165, 180, 214, 151, 111, 161, 233, 147, 124, 143]),
                Is.EqualTo(3176)
            );
        }
    }
}
