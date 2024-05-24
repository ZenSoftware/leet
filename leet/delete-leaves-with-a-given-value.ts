/**
 * https://leetcode.com/problems/delete-leaves-with-a-given-value/?envType=daily-question&envId=2024-05-17
 * Given a binary tree root and an integer target, delete all the leaf nodes with value target.
 * Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).
 */

export function removeLeafNodes(
  root: TreeNode | null,
  target: number
): TreeNode | null {
  function dfs(root: TreeNode | null) {
    if (!root) return;

    if (root.left) dfs(root.left);
    if (root.right) dfs(root.right);
  }

  return null;
}

function isLeaf(node: TreeNode | null): boolean {
  if (!node) return false;
  return !node.left && !node.right;
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

let n1 = new TreeNode(1);
let n2 = new TreeNode(2);
let n3a = new TreeNode(3);
let n3b = new TreeNode(3);
let n3c = new TreeNode(3);
n1.left = n3a;
n1.right = n3c;
n3a.left = n3b;
n3a.right = n2;

console.log();
