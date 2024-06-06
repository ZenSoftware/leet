/**
 * https://leetcode.com/problems/binary-tree-inorder-traversal/description/
 * [Iterative solution](https://www.youtube.com/watch?v=g_S5WuasWUE)
 */
export { inorderTraversal, TreeNode };

function inorderTraversal(root: TreeNode | null): number[] {
  if (!root) return [];

  const stack: TreeNode[] = [];
  const result: number[] = [];
  let current: TreeNode | null = root;

  while (current || stack.length !== 0) {
    while (current) {
      stack.push(current);
      current = current.left;
    }
    current = stack.pop()!;
    result.push(current.val);
    current = current.right;
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
