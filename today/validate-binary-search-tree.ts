/**
 * https://leetcode.com/problems/validate-binary-search-tree/
 */
export { isValidBST, TreeNode };

function isValidBST(root: TreeNode | null): boolean {
  if (!root) return true;

  let leftResult = true;
  let rightResult = true;

  if (root.left) {
    const leftValues = getValues(root.left);
    if (!allLessThan(leftValues, root.val)) return false;
    leftResult = isValidBST(root.left);
  }

  if (root.right) {
    const rightValues = getValues(root.right);
    if (!allGreaterThan(rightValues, root.val)) return false;
    rightResult = isValidBST(root.right);
  }

  return leftResult && rightResult;
}

function allLessThan(elements: number[], value: number) {
  for (let e of elements) {
    if (value <= e) return false;
  }
  return true;
}

function allGreaterThan(elements: number[], value: number) {
  for (let e of elements) {
    if (value >= e) return false;
  }
  return true;
}

function getValues(root: TreeNode | null): number[] {
  const result: number[] = [];
  function dfs(node: TreeNode | null) {
    if (!node) return [];
    result.push(node.val);
    if (node.left) dfs(node.left);
    if (node.right) dfs(node.right);
  }
  dfs(root);
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
