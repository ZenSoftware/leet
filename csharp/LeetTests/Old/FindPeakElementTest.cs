using Leet.FindPeakElement;

namespace LeetTests
{
    internal class FindPeakElementTest
    {
        [Test]
        public void TestFindPeakElement()
        {
            var solution = new Solution();
            Assert.That(solution.FindPeakElement([1, 2, 3, 1]), Is.EqualTo(2));
            Assert.That(solution.FindPeakElement([1, 2, 1, 3, 5, 6, 4]), Is.EqualTo(5));
            Assert.That(solution.FindPeakElement([1]), Is.EqualTo(0));
            Assert.That(solution.FindPeakElement([1, 2]), Is.EqualTo(1));
            Assert.That(solution.FindPeakElement([2, 1]), Is.EqualTo(0));
            Assert.That(solution.FindPeakElement([3, 4, 3, 2, 1]), Is.EqualTo(1));
            Assert.That(solution.FindPeakElement([1, 2, 3, 4, 3]), Is.EqualTo(3));
        }
    }
}