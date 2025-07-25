/**
 * https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
 */
export { sortedListToBST, TreeNode, ListNode };

function sortedListToBST(head: ListNode | null): TreeNode | null {
  if (!head) return null;

  const nums: number[] = [];

  let pointer: ListNode | null = head;
  while (pointer) {
    nums.push(pointer.val);
    pointer = pointer.next;
  }

  function constrcutTree(start: number, end: number): TreeNode | null {
    if (start > end) return null;

    const mid = Math.floor((start + end) / 2);
    const node = new TreeNode(nums[mid]);
    node.left = constrcutTree(start, mid - 1);
    node.right = constrcutTree(mid + 1, end);
    return node;
  }

  return constrcutTree(0, nums.length - 1);
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

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}
