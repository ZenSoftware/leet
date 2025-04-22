using Old.RotateArray;

namespace LeetTests.Old
{
    internal class RotateArrayTest
    {
        [Test]
        public void TestsRotateArray()
        {
            var solution = new Solution();
            var input = new[] { 1, 2, 3, 4, 5, 6, 7 };
            solution.Rotate(input, 3);
            Assert.That(
                input,
                Is.EqualTo(new[] { 5, 6, 7, 1, 2, 3, 4 })
            );
        }

        [Test]
        public void TestsRotateArray2()
        {
            var solution = new Solution();
            var input = new[] { -1, -100, 3, 99 };
            solution.Rotate(input, 2);
            Assert.That(
                input,
                Is.EqualTo(new[] { 3, 99, -1, -100 })
            );
        }

        [Test]
        public void TestsRotateArray3()
        {
            var solution = new Solution();
            var input = new[] { 1, 2, 3, 4, 5 };
            solution.Rotate(input, 1);
            Assert.That(
                input,
                Is.EqualTo(new[] { 5, 1, 2, 3, 4 })
            );
        }


    }
}
