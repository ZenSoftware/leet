/**
 * https://leetcode.com/problems/insertion-sort-list/
 */
export { insertionSortList, ListNode };

function insertionSortList(head: ListNode | null): ListNode | null {
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
