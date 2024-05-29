/**
 * https://leetcode.com/problems/remove-nth-node-from-end-of-list/
 */

export function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  let dummyHead = new ListNode(0, head);
  let right: any = dummyHead;
  let left: any = dummyHead;

  for (let i = 1; i <= n; i++) {
    right = right.next;
  }

  while (right.next) {
    left = left.next;
    right = right.next;
  }

  left.next = left.next.next;

  return dummyHead.next;
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
  let pointer: ListNode | null = list;
  while (pointer) {
    result.push(pointer.val);
    pointer = pointer.next;
  }

  return result;
}
