// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
using Leet.Tree;
namespace Today3.LowestCommonAncestorOfABinaryTree;

public class Solution
{
    public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q)
    {
        TreeNode? result = null;

        bool DFS(TreeNode root)
        {
            if (root == null || result != null)
                return false;

            var inLeft = DFS(root.left);
            var inRight = DFS(root.right);

            if (inLeft && inRight)
                result = root;

            if ((inLeft || inRight) && (p == root || q == root))
                result = root;

            return inLeft || inRight || p == root || q == root;
        }

        DFS(root);
        return result;
    }
}