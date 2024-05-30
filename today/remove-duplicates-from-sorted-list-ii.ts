/**
 * https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
 */
export { deleteDuplicates };

function deleteDuplicates(head: ListNode | null): ListNode | null {
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
