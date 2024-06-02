/**
 * https://leetcode.com/problems/reorder-list/description/
 */
export { reorderList, ListNode };

function reorderList(head: ListNode | null): void {}

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}
