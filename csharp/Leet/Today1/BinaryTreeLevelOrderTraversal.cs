// https://leetcode.com/problems/binary-tree-level-order-traversal/description/
using Leet.Tree;

namespace Leet.BinaryTreeLevelOrderTraversal
{
    public class Solution
    {
        public IList<IList<int>> LevelOrder(TreeNode root)
        {
            if (root == null)
                return [];

            var result = new List<IList<int>>();
            var queue = new LinkedList<TreeNode>([root]);

            while (queue.Count > 0)
            {
                var size = queue.Count;
                var level = new List<int>();

                for (int i = 0; i < size; i++)
                {
                    var node = queue.First.Value;
                    queue.RemoveFirst();
                    level.Add(node.val);

                    if (node.left != null)
                        queue.AddLast(node.left);
                    if (node.right != null)
                        queue.AddLast(node.right);
                }

                result.Add(level);
            }

            return result;
        }
    }
}