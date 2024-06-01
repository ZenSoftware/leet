/**
 * https://leetcode.com/problems/symmetric-tree/description/
 */
export { isSymmetric, TreeNode };

function isSymmetric(root: TreeNode | null): boolean {
  if (!root) return true;
  if (!root.left && !root.right) return true;

  function dfs(p: TreeNode | null, q: TreeNode | null): boolean {
    if (!p && !q) return true;
    if ((!p && q) || (p && !q)) return false;
    if (p!.val !== q!.val) return false;

    return dfs(p!.left, q!.right) && dfs(p!.right, q!.left);
  }

  if (root.left && root.right && root.left.val === root.right.val) {
    return dfs(root.left, root.right);
  }

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
