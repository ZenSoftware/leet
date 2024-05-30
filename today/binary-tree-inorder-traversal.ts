/**
 * https://leetcode.com/problems/binary-tree-inorder-traversal/description/
 */
export { inorderTraversal, TreeNode };

function inorderTraversal(root: TreeNode | null): number[] {
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
