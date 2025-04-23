// https://leetcode.com/problems/binary-tree-maximum-path-sum/
using Leet.Tree;
namespace Today3.BinaryTreeMaximumPathSum;

public class Solution
{
    public int MaxPathSum(TreeNode root)
    {
        int result = root.val;
        int DFS(TreeNode root)
        {
            if (root == null)
                return 0;

            if (root.left == null && root.right == null)
            {
                result = Math.Max(result, root.val);
                return root.val;
            }


            var leftMax = DFS(root.left);
            var rightMax = DFS(root.right);

            var withSplit = root.val + leftMax + rightMax;
            var withoutSplit = root.val + Math.Max(Math.Max(leftMax, rightMax), 0);

            result = Math.Max(result, withSplit);
            result = Math.Max(result, withoutSplit);

            return withoutSplit;
        }
        DFS(root);
        return result;
    }
}