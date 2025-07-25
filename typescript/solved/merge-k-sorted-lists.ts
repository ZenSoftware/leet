/**
 * https://leetcode.com/problems/merge-k-sorted-lists/
 */

export function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
  if (lists.length === 0) return null;
  if (lists.length === 1) return lists[0];

  let result = lists[0];
  for (let i = 1; i < lists.length; i++) {
    result = mergeLists(result, lists[i]);
  }

  return result;
}

export function mergeLists(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  if (!l1) return l2;
  if (!l2) return l1;

  if (l1.val < l2.val) {
    l1.next = mergeLists(l1.next, l2);
    return l1;
  } else {
    l2.next = mergeLists(l1, l2.next);
    return l2;
  }
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
