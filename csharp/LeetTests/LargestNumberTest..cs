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
            Assert.That(solution.LargestNumber([34323, 3432]), Is.EqualTo("343234323"));
            Assert.That(solution.LargestNumber([0, 0]), Is.EqualTo("0"));
        }

        [Test]
        public void TestsMergeSort()
        {
            var solution = new Solution();
            var result = solution.MergeSort(["5", "3", "1", "2", "4"]);
            Assert.That(
                result,
                Is.EqualTo(new[] { "5", "4", "3", "2", "1" })
            );
        }

        [Test]
        public void TestsStringCompare()
        {
            var solution = new Solution();
            Assert.That(solution.CompareStrings("10", "2"), Is.EqualTo(true));

            Assert.That(solution.CompareStrings("3", "3"), Is.EqualTo(true));

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
