/**
 * https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
 */
export { _Node, connect };

function connect(root: _Node | null): _Node | null {
  return null;
}

class _Node {
  val: number;
  left: _Node | null;
  right: _Node | null;
  next: _Node | null;
  constructor(val?: number, left?: _Node, right?: _Node, next?: _Node) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
    this.next = next === undefined ? null : next;
  }
}
