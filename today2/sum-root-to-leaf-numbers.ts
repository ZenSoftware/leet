/**
 * https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
 */
export { sumNumbers, TreeNode };

function sumNumbers(root: TreeNode | null): number {
  if (!root) return 0;

  let total = 0;

  function dfs(node: TreeNode, path: number[]) {
    path.push(node.val);
    if (!node.left && !node.right) {
      const strNum = path.reduce((accum, curr) => (accum += curr.toString()), '');
      total += Number.parseInt(strNum);
    }
    if (node.left) dfs(node.left, path);
    if (node.right) dfs(node.right, path);
    path.pop();
  }

  dfs(root, []);

  return total;
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
