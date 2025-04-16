// https://leetcode.com/problems/binary-tree-right-side-view/description/
using Leet.Tree;

namespace Leet.BinaryTreeRightSideView
{
    public class Solution
    {
        Dictionary<int, List<TreeNode>> levelOrder;

        public IList<int> RightSideView(TreeNode root)
        {
            levelOrder = new Dictionary<int, List<TreeNode>>();
            LevelOrder(root, 0);
            var result = new List<int>();
            foreach (var (level, nodes) in levelOrder)
            {
                result.Add(nodes[nodes.Count - 1].val);
            }
            return result;
        }

        public void LevelOrder(TreeNode root, int level)
        {
            if (root == null) return;

            if (!levelOrder.ContainsKey(level)) levelOrder.Add(level, new List<TreeNode>());
            levelOrder[level].Add(root);

            LevelOrder(root.left, level + 1);
            LevelOrder(root.right, level + 1);
        }
    }
}
