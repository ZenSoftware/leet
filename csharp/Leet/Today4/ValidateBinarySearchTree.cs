// https://leetcode.com/problems/validate-binary-search-tree/description/
using Leet.Tree;
namespace Today4.ValidateBinarySearchTree;

public class Solution
{
    public bool IsValidBST(TreeNode root)
    {
        bool Traverse(TreeNode root, long min, long max)
        {
            if (root == null)
                return true;
            if (min >= root.val || root.val >= max)
                return false;
            return Traverse(root.left, min, root.val)
                && Traverse(root.right, root.val, max);
        }
        return Traverse(root, long.MinValue, long.MaxValue);
    }
}