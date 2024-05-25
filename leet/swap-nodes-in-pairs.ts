/**
 * https://leetcode.com/problems/swap-nodes-in-pairs/
 */
export function swapPairs(head: ListNode | null): ListNode | null {
  if (!head) return null;
  if (!head.next) return head;

  const dummyHead = new ListNode(undefined, head);
  let p: any = dummyHead;

  while (p?.next && p?.next?.next) {
    let p1 = p;
    let p2 = p.next;
    let p3 = p.next.next;

    const p4 = p3?.next ?? null;
    p2.next = p4;
    p3.next = p2;
    p1.next = p3;

    p = p.next?.next;
  }

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
