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

export function toList(elements: number[]) {
  if (elements.length === 0) return null;

  let pointer: ListNode | null = null;

  for (let i = elements.length - 1; i >= 0; i--) {
    const node = new ListNode(elements[i]);
    node.next = pointer;
    pointer = node;
  }

  return pointer;
}

export function toArray(list: ListNode | null) {
  if (!list) return [];

  const result: number[] = [];

  while (list) {
    result.push(list.val);
    list = list.next;
  }

  return result;
}
