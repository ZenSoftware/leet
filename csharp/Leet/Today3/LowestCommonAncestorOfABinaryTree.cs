// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
using Leet.Tree;
namespace Today3.LowestCommonAncestorOfABinaryTree;

public class Solution
{
    public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q)
    {
        if (root == null || root == p || root == q)
            return root;

        var left = LowestCommonAncestor(root.left, p, q);
        var right = LowestCommonAncestor(root.right, p, q);

        if (left != null && right != null)
            return root;

        return left != null ? left : right;
    }
}