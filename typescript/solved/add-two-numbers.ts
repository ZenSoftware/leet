/**
 * https://leetcode.com/problems/add-two-numbers/description/
 *
 * You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
 *
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 */

export function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  if (l1 === null) return l2;
  if (l2 === null) return l1;

  let p1: ListNode | null = l1;
  let p2: ListNode | null = l2;
  let resultHead = new ListNode();
  let resultPointer = resultHead;
  let carry = 0;

  while (p1 || p2) {
    if (p1 === null) {
      let val = p2!.val + carry;
      if (val >= 10) {
        val = val - 10;
        carry = 1;
      } else {
        carry = 0;
      }
      resultPointer.next = new ListNode(val);
      resultPointer = resultPointer.next;
      p2 = p2!.next;
      continue;
    }

    if (p2 === null) {
      let val = p1!.val + carry;
      if (val >= 10) {
        val = val - 10;
        carry = 1;
      } else {
        carry = 0;
      }
      resultPointer.next = new ListNode(val);
      resultPointer = resultPointer.next;
      p1 = p1!.next;
      continue;
    }

    let val = p1.val + p2.val + carry;
    if (val >= 10) {
      val = val - 10;
      carry = 1;
    } else {
      carry = 0;
    }

    resultPointer.next = new ListNode(val);

    resultPointer = resultPointer.next;
    p1 = p1.next;
    p2 = p2.next;
  }

  if (carry > 0) resultPointer.next = new ListNode(1);

  return resultHead.next;
}

export class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

export function toList(list: number[]) {
  if (list.length === 0) return null;

  let prev: ListNode | null = null;

  for (let i = list.length - 1; i >= 0; i--) {
    const node = new ListNode(list[i]);
    node.next = prev;
    prev = node;
  }

  return prev;
}

export function toArray(list: ListNode | null) {
  if (!list) return [];

  const result: number[] = [];
  let pointer: ListNode | null = list;

  do {
    result.push(pointer.val);
    pointer = pointer.next;
  } while (pointer);

  return result;
}
