/**
 * https://leetcode.com/problems/insertion-sort-list/
 */
export { insertionSortList, ListNode };

function insertionSortList(head: ListNode | null): ListNode | null {
  if (!head) return null;

  const nodes: ListNode[] = [];
  let pointer: ListNode | null = head;
  while (pointer) {
    nodes.push(pointer);
    pointer = pointer.next;
  }

  nodes.sort((a, b) => a.val - b.val);

  for (let k = 0; k < nodes.length - 1; k++) {
    nodes[k].next = nodes[k + 1];
  }
  nodes[nodes.length - 1].next = null;

  return nodes[0];
}

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}
