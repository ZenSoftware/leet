/**
 * https://leetcode.com/problems/merge-k-sorted-lists/
 */

export function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
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
