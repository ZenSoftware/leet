/**
 * https://leetcode.com/problems/path-sum/description/
 */
export { hasPathSum, TreeNode };

function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
  if (!root) return false;

  let result = false;
  function dfs(node: TreeNode, sum: number) {
    sum += node.val;
    if (!node.left && !node.right && sum === targetSum) {
      result = true;
      return;
    }
    if (node.left) dfs(node.left, sum);
    if (node.right) dfs(node.right, sum);
  }

  dfs(root, 0);
  return result;
}

class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}
