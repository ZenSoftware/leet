using Leet.SameTree;

namespace LeetTests
{
    internal class SameTreeTest
    {
        [Test]
        public void TestSameTree1()
        {
            var solution = new Solution();
            var p1 = new TreeNode(1);
            var p2 = new TreeNode(2);
            var p3 = new TreeNode(3);
            p1.left = p2;
            p1.right = p3;

            var q1 = new TreeNode(1);
            var q2 = new TreeNode(2);
            var q3 = new TreeNode(3);
            q1.left = q2;
            q1.right = q3;

            Assert.That(
                solution.IsSameTree(p1, q1),
                Is.EqualTo(true)
            );
        }

        [Test]
        public void TestSameTree2()
        {
            var solution = new Solution();
            var p1 = new TreeNode(1);
            var p2 = new TreeNode(2);
            p1.left = p2;

            var q1 = new TreeNode(1);
            var q2 = new TreeNode(2);
            q1.right = q2;

            Assert.That(
                solution.IsSameTree(p1, q1),
                Is.EqualTo(false)
            );
        }

        [Test]
        public void TestSameTree3()
        {
            var solution = new Solution();
            var p1 = new TreeNode(1);
            var p1b = new TreeNode(1);
            var p2 = new TreeNode(2);
            p1.left = p2;
            p1.right = p1b;

            var q1 = new TreeNode(1);
            var q1b = new TreeNode(1);
            var q2 = new TreeNode(2);
            q1.left = q1b;
            q1.right = q2;

            Assert.That(
                solution.IsSameTree(p1, q1),
                Is.EqualTo(false)
            );
        }
    }
}
