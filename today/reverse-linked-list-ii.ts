/**
 * https://leetcode.com/problems/reverse-linked-list-ii/description/
 */
export { reverseBetween, toList, toArray };

function reverseBetween(head: ListNode | null, left: number, right: number): ListNode | null {
  if (!head?.next) return head;

  let dummyHead = new ListNode(Infinity, head);
  let pointer: ListNode | null = dummyHead;
  const rotateElements: ListNode[] = [];

  let l = 1;
  while (l < left) {
    pointer = pointer!.next;
    l++;
  }

  let pointerBefore = pointer;
  pointer = pointer!.next;

  let r = l;
  while (r < right) {
    rotateElements.push(pointer as ListNode);
    pointer = pointer!.next;
    r++;
  }
  rotateElements.push(pointer as ListNode);

  let pointerAfter = pointer!.next;

  for (let i = rotateElements.length - 1; i >= 1; i--) {
    rotateElements[i].next = rotateElements[i - 1];
  }

  pointerBefore!.next = rotateElements[rotateElements.length - 1];
  rotateElements[0].next = pointerAfter;

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

function toList(elements: number[]): ListNode | null {
  if (elements.length === 0) return null;
  let prev: ListNode | null = null;
  for (let i = elements.length - 1; i >= 0; i--) {
    const node = new ListNode(elements[i]);
    node.next = prev;
    prev = node;
  }
  return prev;
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
