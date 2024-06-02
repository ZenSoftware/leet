/**
 * https://leetcode.com/problems/reorder-list/description/
 */
export { reorderList, toArray, toList, ListNode };

function reorderList(head: ListNode | null): void {}

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function toList(elements: number[]): ListNode | null {
  if (elements.length === 0) return null;
  let pointer: ListNode | null = null;
  for (let i = elements.length - 1; i >= 0; i--) {
    const node = new ListNode(elements[i]);
    node.next = pointer;
    pointer = node;
  }
  return pointer;
}

function toArray(list: ListNode | null): number[] {
  if (!list) return [];
  const result: number[] = [];
  while (list) {
    result.push(list.val);
    list = list.next;
  }
  return result;
}
