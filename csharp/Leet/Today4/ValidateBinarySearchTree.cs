// https://leetcode.com/problems/validate-binary-search-tree/description/
using Leet.Tree;
namespace Today4.ValidateBinarySearchTree;

public class Solution
{
    public bool IsValidBST(TreeNode root)
    {
        if (root == null)
            return true;
        if (root.left != null && root.left.val >= root.val)
            return false;
        if (root.right != null && root.right.val <= root.val)
            return false;
        return IsValidBST(root.left) && IsValidBST(root.right);
    }
}