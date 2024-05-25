/**
 * https://leetcode.com/problems/remove-nth-node-from-end-of-list/
 */

export function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
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
