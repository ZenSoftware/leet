/**
 * https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
 */
export { sortedArrayToBST, TreeNode };

function sortedArrayToBST(nums: number[]): TreeNode | null {
  function construct(start: number, end: number): TreeNode | null {
    if (start > end) return null;

    const mid = Math.floor((start + end) / 2);
    const node = new TreeNode(nums[mid]);
    node.left = construct(start, mid - 1);
    node.right = construct(mid + 1, end);
    return node;
  }

  return construct(0, nums.length - 1);
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
