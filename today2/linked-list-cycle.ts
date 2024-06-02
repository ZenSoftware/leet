/**
 * https://leetcode.com/problems/linked-list-cycle/description/
 */
export { hasCycle, ListNode };

function hasCycle(head: ListNode | null): boolean {
  const cache = new Set<ListNode>();

  let pointer = head;
  while (pointer) {
    if (cache.has(pointer)) return true;
    else cache.add(pointer);
    pointer = pointer.next;
  }

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
