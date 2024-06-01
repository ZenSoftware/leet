/**
 * https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
 */
export { maxDepth, TreeNode };

function maxDepth(root: TreeNode | null): number {
  return -1;
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
