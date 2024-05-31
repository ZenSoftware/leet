/**
 * https://leetcode.com/problems/unique-binary-search-trees-ii/
 */
export { generateTrees, TreeNode };

function generateTrees(n: number): Array<TreeNode | null> {
  function dfs(start: number, end: number) {
    if (end < start) return [null];
    if (end === start) return [new TreeNode(end)];

    const trees: TreeNode[] = [];

    for (let i = start; i <= end; i++) {
      const leftTrees = dfs(start, i - 1);
      const rightTrees = dfs(i + 1, end);

      for (const left of leftTrees) {
        for (const right of rightTrees) {
          trees.push(new TreeNode(i, left, right));
        }
      }
    }

    return trees;
  }

  return dfs(1, n);
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
