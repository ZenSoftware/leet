// https://leetcode.com/problems/subtree-of-another-tree/description/
using Leet.Tree;
namespace Today3.SubtreeOfAnotherTree;

public class Solution
{
    public bool IsSubtree(TreeNode root, TreeNode subRoot)
    {
        TreeNode? FindSubtree(TreeNode root)
        {
            if (root == null || root.val == subRoot.val)
                return root;
            var left = FindSubtree(root.left);
            if (left != null)
                return left;
            return FindSubtree(root.right);
        }

        var s = FindSubtree(root);
        if (s == null)
            return false;

        bool TreesEqual(TreeNode a, TreeNode b)
        {
            if (a == null && b == null)
                return true;
            if (a?.val != b?.val)
                return false;
            return TreesEqual(a.left, b.left) && TreesEqual(a.right, b.right);
        }

        return TreesEqual(s, subRoot);
    }
}