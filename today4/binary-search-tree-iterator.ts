/**
 *
 */
export { BSTIterator, TreeNode };

class BSTIterator {
  stack: TreeNode[] = [];

  constructor(root: TreeNode | null) {
    let pointer = root;
    while (pointer) {
      this.stack.push(pointer!);
      pointer = pointer!.left;
    }
  }

  next(): number {
    const next = this.stack.pop();
    if (next!.right) this.stack.push(next!.right);
    return next!.val;
  }

  hasNext(): boolean {
    return !!this.stack.length;
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
