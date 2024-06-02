/**
 * https://leetcode.com/problems/linked-list-cycle-ii/description/
 */
export { detectCycle, ListNode };

function detectCycle(head: ListNode | null): ListNode | null {
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
