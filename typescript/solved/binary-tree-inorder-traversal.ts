/**
 * https://leetcode.com/problems/binary-tree-inorder-traversal/description/
 */
export { inorderTraversal, TreeNode };

function inorderTraversal(root: TreeNode | null): number[] {
  const result: number[] = [];

  function dfs(node: TreeNode | null) {
    if (!node) return;

    if (node.left) dfs(node.left);
    result.push(node.val);
    if (node.right) dfs(node.right);
  }

  dfs(root);
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
