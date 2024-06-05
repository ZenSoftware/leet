namespace LeetTests
{
    internal class LeetListTest
    {
        [Test]
        public void ConstructsList()
        {
            int[] input = { 1, 2, 3, 4 };
            var list = LeetList.ToList(input);
            var result = LeetList.ToArray(list);
            Assert.That(result, Is.EqualTo(input));
        }

        [Test]
        public void ConstructsEmptyList()
        {
            var list = LeetList.ToList([]);
            var result = LeetList.ToArray(list);
            Assert.That(result, Is.Empty);
        }
    }
}
