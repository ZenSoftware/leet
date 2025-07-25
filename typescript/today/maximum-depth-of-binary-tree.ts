/**
 * https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
 */
export { maxDepth, TreeNode };

function maxDepth(root: TreeNode | null): number {
  if (!root) return 0;

  let max = 0;

  function dfs(node: TreeNode, level: number) {
    if (level > max) max = level;

    if (node.left) dfs(node.left, level + 1);
    if (node.right) dfs(node.right, level + 1);
  }

  dfs(root, 1);
  return max;
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
