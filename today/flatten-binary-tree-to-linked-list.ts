/**
 * https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
 */
export { flatten, TreeNode };

function flatten(root: TreeNode | null): void {
  if (!root) return;

  const nodes: TreeNode[] = [];
  function dfs(node: TreeNode) {
    nodes.push(node);
    if (node.left) dfs(node.left);
    if (node.right) dfs(node.right);
  }

  dfs(root);

  for (let i = 0; i < nodes.length - 1; i++) {
    nodes[i].left = null;
    nodes[i].right = nodes[i + 1];
  }
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
