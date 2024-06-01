/**
 * https://leetcode.com/problems/balanced-binary-tree/
 */
export { isBalanced, TreeNode };

function isBalanced(root: TreeNode | null): boolean {
  if (!root) return true;

  function dfs(node: TreeNode): Info {
    let leftInfo: Info = { balanced: true, height: 1 };
    if (node.left) {
      leftInfo = dfs(node.left);
    }

    let rightInfo: Info = { balanced: true, height: 1 };
    if (node.right) {
      rightInfo = dfs(node.right);
    }

    const isBalanced = Math.abs(leftInfo.height - rightInfo.height) <= 1;

    return {
      balanced: leftInfo.balanced && rightInfo.balanced && isBalanced,
      height: Math.max(leftInfo.height, rightInfo.height) + 1,
    };
  }

  const result = dfs(root);
  return result.balanced;
}

interface Info {
  balanced: boolean;
  height: number;
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
