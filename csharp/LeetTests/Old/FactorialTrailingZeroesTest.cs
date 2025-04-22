using Old.FactorialTrailingZeroes;

namespace Old
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
            Assert.That(soltuion.TrailingZeroes(25), Is.EqualTo(6));
        }
    }
}
