// https://leetcode.com/problems/binary-tree-level-order-traversal/description/
using Leet.Tree;
namespace Today1.BinaryTreeLevelOrderTraversal;

public class Solution
{
    public IList<IList<int>> LevelOrder(TreeNode root)
    {
        if (root == null)
            return [];

        var result = new List<IList<int>>();
        var queue = new Queue<TreeNode>([root]);

        while (queue.Count > 0)
        {
            var size = queue.Count;
            var level = new List<int>(size);

            for (int i = 0; i < size; i++)
            {
                var node = queue.Dequeue();
                level.Add(node.val);

                if (node.left != null)
                    queue.Enqueue(node.left);

                if (node.right != null)
                    queue.Enqueue(node.right);
            }

            result.Add(level);
        }

        return result;
    }
}

public class Solution2
{
    /// Time: O(n)
    /// Space: O(1)
    public IList<IList<int>> LevelOrder(TreeNode root)
    {
        var levels = new List<IList<int>>();

        void DFS(TreeNode root, int i)
        {
            if (root == null)
                return;

            if (levels.Count - 1 < i)
                levels.Add([]);

            levels[i].Add(root.val);

            DFS(root.left, i + 1);
            DFS(root.right, i + 1);
        }

        DFS(root, 0);
        return levels;
    }
}