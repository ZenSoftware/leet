using Old.MajorityElement;

namespace Old
{
    internal class MajorityElementTest
    {
        [Test]
        public void TestMajorityElement()
        {
            var solution = new Solution();
            Assert.That(solution.MajorityElement([3, 2, 3]), Is.EqualTo(3));
            Assert.That(solution.MajorityElement([2, 2, 1, 1, 1, 2, 2]), Is.EqualTo(2));
        }
    }
}
