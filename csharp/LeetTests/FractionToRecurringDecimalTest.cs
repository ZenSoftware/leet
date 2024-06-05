using Leet.FractionToRecurringDecimal;

namespace LeetTests
{
    public class FractionToRecurringDecimalTest
    {
        [Test]
        public void TestFractionToRecurringDecimal()
        {
            var solution = new Solution();
            Assert.That(solution.FractionToDecimal(1, 2), Is.EqualTo("0.5"));
            Assert.That(solution.FractionToDecimal(2, 1), Is.EqualTo("2"));
            Assert.That(solution.FractionToDecimal(4, 333), Is.EqualTo("0.(012)"));
        }
    }
}
