// https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
using Leet.Tree;
namespace Today4.KthSmallestElementInABST;

public class Solution
{
    public int KthSmallest(TreeNode root, int k)
    {
        var inorder = new List<int>();
        void DFS(TreeNode root)
        {
            if (root == null || inorder.Count >= k)
                return;
            DFS(root.left);
            inorder.Add(root.val);
            DFS(root.right);
        }
        DFS(root);

        return inorder[k - 1];
    }
}