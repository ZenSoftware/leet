using Leet.BinaryTreeLevelOrderTraversal;

namespace LeetTests
{
    internal class BinaryTreeLevelOrderTraversalTest
    {
        [Test]
        public void TestBinaryTreeLevelOrderTraversal()
        {
            var n3 = new TreeNode(3);
            var n9 = new TreeNode(9);
            var n20 = new TreeNode(20);
            var n15 = new TreeNode(15);
            var n7 = new TreeNode(7);
            n3.left = n9;
            n3.right = n20;
            n20.left = n15;
            n20.right = n7;

            var solution = new Solution();
            Assert.That(
                solution.LevelOrder(n3),
                Is.EquivalentTo(new[] { new[] { 3 }, new[] { 9, 20 }, new[] { 15, 7 } })
            );
        }

        [Test]
        public void TestBinaryTreeLevelOrderTraversal2()
        {
            var n3 = new TreeNode(3);
            var n9 = new TreeNode(9);
            var n20 = new TreeNode(20);
            var n15 = new TreeNode(15);
            var n7 = new TreeNode(7);
            n3.left = n9;
            n3.right = n20;
            n20.left = n15;
            n20.right = n7;

            var solution = new Solution2();
            Assert.That(
                solution.LevelOrder(n3),
                Is.EquivalentTo(new[] { new[] { 3 }, new[] { 9, 20 }, new[] { 15, 7 } })
            );
        }
    }
}
