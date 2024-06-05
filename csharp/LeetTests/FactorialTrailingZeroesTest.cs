using Leet.FactorialTrailingZeroes;

namespace LeetTests
{
    internal class FactorialTrailingZeroesTest
    {
        [Test]
        public void TestTrailingZeroes()
        {
            var soltuion = new Solution();
            Assert.That(soltuion.TrailingZeroes(3), Is.EqualTo(0));
            Assert.That(soltuion.TrailingZeroes(5), Is.EqualTo(1));
            Assert.That(soltuion.TrailingZeroes(0), Is.EqualTo(0));
            Assert.That(soltuion.TrailingZeroes(13), Is.EqualTo(2));
        }

        [Test]
        public void TestFactorial()
        {
            var soltuion = new Solution();
            Assert.That(soltuion.Factorial(13), Is.EqualTo(6227020800));
            Assert.That(soltuion.Factorial(5), Is.EqualTo(120));
            Assert.That(soltuion.Factorial(4), Is.EqualTo(24));
            Assert.That(soltuion.Factorial(3), Is.EqualTo(6));
            Assert.That(soltuion.Factorial(2), Is.EqualTo(2));
            Assert.That(soltuion.Factorial(1), Is.EqualTo(1));
        }
    }
}
