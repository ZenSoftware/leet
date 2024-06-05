using Leet.CompareVersionNumbers;

namespace LeetTests
{
    public class CompareVersionNumbersTest
    {
        [Test]
        public void TestCompareVersionNumbers()
        {
            var solution = new Solution();
            Assert.That(solution.CompareVersion("1.2", "1.10"), Is.EqualTo(-1));
            Assert.That(solution.CompareVersion("1.01", "1.001"), Is.EqualTo(-1));
            Assert.That(solution.CompareVersion("1.0", "1.0.0.0"), Is.EqualTo(-1));
        }
    }
}
