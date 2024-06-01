/**
 * https://leetcode.com/problems/path-sum/description/
 */
export { hasPathSum, TreeNode };

function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
  return false;
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
