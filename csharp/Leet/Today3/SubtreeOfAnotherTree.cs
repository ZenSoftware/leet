// https://leetcode.com/problems/subtree-of-another-tree/description/
using Leet.Tree;
namespace Today3.SubtreeOfAnotherTree;

public class Solution
{
    public bool IsSubtree(TreeNode root, TreeNode subRoot)
    {
        if (root == null)
            return false;
        if (TreesEqual(root, subRoot))
            return true;
        return IsSubtree(root.left, subRoot) || IsSubtree(root.right, subRoot);
    }

    private bool TreesEqual(TreeNode a, TreeNode b)
    {
        if (a?.val != b?.val)
            return false;
        if (a == null && b == null)
            return true;
        return TreesEqual(a.left, b.left) && TreesEqual(a.right, b.right);
    }
}