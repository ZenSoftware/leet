/**
 * https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
 */
export { minDepth, TreeNode };

function minDepth(root: TreeNode | null): number {
  if (!root) return 0;

  let minimum = Infinity;

  function dfs(node: TreeNode, level: number) {
    if (!node.left && !node.right && level < minimum) minimum = level;
    if (node.left) dfs(node.left, level + 1);
    if (node.right) dfs(node.right, level + 1);
  }

  dfs(root, 1);
  return minimum;
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
