using Old.BinaryTreeRightSideView;

namespace Old
{
    internal class BinaryTreeRightSideViewTest
    {
        [Test]
        public void TestsBinaryTreeRightSideView()
        {
            var solution = new Solution();
            var n1 = new TreeNode(1);
            var n2 = new TreeNode(2);
            var n3 = new TreeNode(3);
            var n4 = new TreeNode(4);
            var n5 = new TreeNode(5);
            n1.left = n2;
            n1.right = n3;
            n2.right = n5;
            n3.right = n4;
            Assert.That(
                solution.RightSideView(n1),
                Is.EqualTo(new[] { 1, 3, 4 })
            );
        }
    }
}
