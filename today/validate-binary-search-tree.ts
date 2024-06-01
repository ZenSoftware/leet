/**
 * https://leetcode.com/problems/validate-binary-search-tree/
 */
export { isValidBST, TreeNode };

function isValidBST(root: TreeNode) {
  if (root.left) {
    if (root.left.val >= root.val) return false;
    return isValidBST(root.left);
  }

  if (root.right) {
    if (root.right.val <= root.val) return false;
    return isValidBST(root.right);
  }

  return true;
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
