// https://leetcode.com/problems/subtree-of-another-tree/description/
using Leet.Tree;
namespace Today3.SubtreeOfAnotherTree;

public class Solution
{
    public bool IsSubtree(TreeNode root, TreeNode subRoot)
    {
        var possibleSubTrees = GetPossibleSubTrees(root, subRoot);
        if (possibleSubTrees.Count == 0)
            return false;

        foreach (var tree in possibleSubTrees)
        {
            if (TreesEqual(tree, subRoot))
                return true;
        }

        return false;
    }

    private bool TreesEqual(TreeNode a, TreeNode b)
    {
        if (a == null && b == null)
            return true;
        if (a?.val != b?.val)
            return false;
        return TreesEqual(a.left, b.left) && TreesEqual(a.right, b.right);
    }

    private List<TreeNode> GetPossibleSubTrees(TreeNode root, TreeNode subRoot)
    {
        var trees = new List<TreeNode>();

        void FindSubtree(TreeNode root)
        {
            if (root == null)
                return;
            if (root.val == subRoot.val)
                trees.Add(root);
            FindSubtree(root.left);
            FindSubtree(root.right);
        }

        FindSubtree(root);
        return trees;
    }
}