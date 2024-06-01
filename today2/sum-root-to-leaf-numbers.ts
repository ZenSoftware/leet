/**
 * https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
 */
export { sumNumbers, TreeNode };

function sumNumbers(root: TreeNode | null): number {
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
