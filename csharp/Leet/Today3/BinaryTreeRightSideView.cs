// https://leetcode.com/problems/binary-tree-right-side-view/description/
namespace Today3.BinaryTreeRightSideView;
using Leet.Tree;

public class Solution
{
    public IList<int> RightSideView(TreeNode root)
    {
        if (root == null)
            return [];

        var result = new List<int>();
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);

        while (queue.Count > 0)
        {
            result.Add(queue.Last().val);
            var size = queue.Count;
            for (int i = 0; i < size; i++)
            {
                var node = queue.Dequeue();
                if (node.left != null)
                    queue.Enqueue(node.left);
                if (node.right != null)
                    queue.Enqueue(node.right);
            }
        }

        return result;
    }
}