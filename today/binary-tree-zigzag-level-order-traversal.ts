/**
 * https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
 */
export { zigzagLevelOrder, TreeNode };

function zigzagLevelOrder(root: TreeNode | null): number[][] {
  if (!root) return [];

  const map = new Map<number, number[]>();

  function dfs(node: TreeNode, level: number) {
    let result = map.get(level);

    if (!result) {
      result = [];
      map.set(level, result);
    }

    result.push(node.val);

    if (node.left) dfs(node.left, level + 1);
    if (node.right) dfs(node.right, level + 1);
  }

  dfs(root, 0);

  const result = Array.from(map.values());

  for (let i = 1; i < result.length; i += 2) {
    result[i].reverse();
  }

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
