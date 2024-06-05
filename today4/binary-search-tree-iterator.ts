/**
 *
 */
export { BSTIterator, TreeNode };

class BSTIterator {
  current = 0;
  inOrderValues: number[] = [];

  constructor(private root: TreeNode | null) {
    this.inOrderValues = this.inOrder(root!);
  }

  inOrder(root: TreeNode) {
    const result: number[] = [];
    function bs(node: TreeNode) {
      if (node.left) bs(node.left);
      result.push(node.val);
      if (node.right) bs(node.right);
    }
    bs(root);
    return result;
  }

  next(): number {
    const result = this.inOrderValues[this.current];
    this.current++;
    return result;
  }

  hasNext(): boolean {
    return this.current < this.inOrderValues.length;
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
