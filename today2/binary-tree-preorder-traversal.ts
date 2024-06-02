/**
 * https://leetcode.com/problems/binary-tree-preorder-traversal/description/
 */
export { preorderTraversal, TreeNode };

function preorderTraversal(root: TreeNode | null): number[] {
  return [];
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
