/**
 * https://leetcode.com/problems/path-sum-ii/
 */
export { pathSum, TreeNode };

function pathSum(root: TreeNode | null, targetSum: number): number[][] {
  if (!root) return [];

  const result: number[][] = [];

  function dfs(node: TreeNode, path: number[]) {
    if (!node.left && !node.right) {
      const sum = path.reduce((prev, cur) => prev + cur, 0) + node.val;
      if (sum === targetSum) result.push([...path, node.val]);
    }

    path.push(node.val);
    if (node.left) dfs(node.left, path);
    if (node.right) dfs(node.right, path);
    path.pop();
  }

  dfs(root, []);
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
