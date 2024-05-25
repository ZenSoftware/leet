/**
 * https://leetcode.com/problems/swap-nodes-in-pairs/
 */
export function swapPairs(head: ListNode | null): ListNode | null {
  return null;
}

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}
