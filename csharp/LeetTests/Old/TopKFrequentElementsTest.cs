using Old.TopKFrequentElements;

namespace Old
{
    internal class TopKFrequentElementsTest
    {
        [Test]
        public void TestTopKFrequentElementsTest()
        {
            var solution = new Solution();

            Assert.That(
                solution.TopKFrequent([1, 1, 1, 2, 2, 3], 2),
                Is.EqualTo(new int[] { 1, 2 })
            );
        }
    }
}
