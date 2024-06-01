/**
 * https://leetcode.com/problems/path-sum-ii/
 */
export { pathSum, TreeNode };

function pathSum(root: TreeNode | null, targetSum: number): number[][] {
  const result: number[][] = [];

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
