/**
 * https://leetcode.com/problems/unique-binary-search-trees-ii/
 */
export { generateTrees, TreeNode };

function generateTrees(n: number): Array<TreeNode | null> {
  return [];
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
