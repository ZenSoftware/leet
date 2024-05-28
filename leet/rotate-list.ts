/**
 * https://leetcode.com/problems/rotate-list/
 */
export function rotateRight(head: ListNode | null, k: number): ListNode | null {
  if (!head) return null;

  const length = count(head);
  k = k % length;

  for (let i = 1; i <= k; i++) {
    head = rotateOnce(head);
  }

  return head;
}

export function rotateOnce(head: ListNode | null): ListNode | null {
  if (!head) return null;
  if (!head.next) return head;

  const dummyHead = new ListNode(-Infinity, head);

  let pointer: ListNode | null = head!.next;
  let trailingPointer: ListNode | null = head;
  while (pointer!.next) {
    pointer = pointer!.next;
    trailingPointer = trailingPointer!.next as ListNode;
  }

  trailingPointer!.next = null;
  pointer!.next = dummyHead.next;
  dummyHead.next = pointer;

  return dummyHead.next as ListNode;
}

function count(list: ListNode | null): number {
  let counter = 0;
  while (list) {
    counter++;
    list = list.next;
  }
  return counter;
}

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

export function toList(elements: number[]): ListNode | null {
  if (elements.length === 0) return null;

  let pointer: ListNode | null = null;
  for (let i = elements.length - 1; i >= 0; i--) {
    const node = new ListNode(elements[i]);
    node.next = pointer;
    pointer = node;
  }
  return pointer;
}

export function toArray(list: ListNode | null): number[] {
  if (!list) return [];

  const result: number[] = [];
  while (list) {
    result.push(list.val);
    list = list.next;
  }
  return result;
}
