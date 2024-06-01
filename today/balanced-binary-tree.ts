/**
 * https://leetcode.com/problems/balanced-binary-tree/
 */
export { isBalanced, TreeNode };

function isBalanced(root: TreeNode | null): boolean {
  if (!root) return true;

  let depth = 0;
  let count = 0;

  function dfs(node: TreeNode, level: number) {
    if (level > depth) depth = level;
    count++;
    if (node.left) dfs(node.left, level + 1);
    if (node.right) dfs(node.right, level + 1);
  }

  dfs(root, 1);
  const balancedHeight = Math.floor(Math.log2(count));
  return depth <= balancedHeight + 1;
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
