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

        [Test]
        public void TestsMergeSort()
        {
            var solution = new Solution();
            Assert.That(
                solution.MergeSort(["5", "3", "1", "2", "4"]),
                Is.EqualTo(new[] { "1", "2", "3", "4", "5" })
            );
        }

        [Test]
        public void TestsStringCompare()
        {
            var solution = new Solution();
            Assert.That(solution.CompareStrings("10", "2"), Is.EqualTo(true));

            Assert.That(solution.CompareStrings("3", "4"), Is.EqualTo(true));
            Assert.That(solution.CompareStrings("33", "34"), Is.EqualTo(true));

            Assert.That(solution.CompareStrings("34", "33"), Is.EqualTo(false));
            Assert.That(solution.CompareStrings("334", "33"), Is.EqualTo(false));

            Assert.That(solution.CompareStrings("30", "3"), Is.EqualTo(true));
            Assert.That(solution.CompareStrings("330", "33"), Is.EqualTo(true));

            Assert.That(solution.CompareStrings("3", "30"), Is.EqualTo(false));
            Assert.That(solution.CompareStrings("33", "330"), Is.EqualTo(false));

            Assert.That(solution.CompareStrings("34323", "3432"), Is.EqualTo(true));
        }
    }
}
