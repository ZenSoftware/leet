/**
 * https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
 */
export { flatten, TreeNode };

function flatten(root: TreeNode | null): void {
  if (!root) return;
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
