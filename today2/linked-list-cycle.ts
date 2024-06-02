/**
 * https://leetcode.com/problems/linked-list-cycle/description/
 */
export { hasCycle, ListNode };

function hasCycle(head: ListNode | null): boolean {
  return false;
}

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}
