/**
 * https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
 */
export { sortedArrayToBST, TreeNode };

function sortedArrayToBST(nums: number[]): TreeNode | null {
  return null;
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
