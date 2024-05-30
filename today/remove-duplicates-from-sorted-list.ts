/**
 * https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
 */
export { deleteDuplicates, toList, toArray };

function deleteDuplicates(head: ListNode | null): ListNode | null {
  if (!head?.next) return head;

  let dummyHead: ListNode | null = new ListNode(-Infinity, head);

  let parent: ListNode | null = dummyHead;
  let pointer: ListNode | null = dummyHead.next;

  while (pointer) {
    if (parent!.val === pointer.val) {
      while (pointer && parent!.val === pointer.val) {
        pointer = pointer.next;
      }
      parent!.next = pointer;
    }

    parent = parent!.next;
    pointer = pointer?.next as any;
  }

  return dummyHead.next;
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

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}
