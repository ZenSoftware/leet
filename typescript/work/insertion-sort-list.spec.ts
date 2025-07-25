import { insertionSortList, ListNode } from './insertion-sort-list';

describe('Insertion Sort List', () => {
  it('evaluates correctly', () => {
    const input = toList([4, 6, 8, 3, 9, 1, 0, 2, 5, 7]);
    const solution = insertionSortList(input);
    expect(toArray(solution)).toEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
  });
});

function toList(elements: number[]) {
  if (elements.length === 0) return null;
  let pointer: ListNode | null = null;
  for (let i = elements.length - 1; i >= 0; i--) {
    const node = new ListNode(elements[i]);
    node.next = pointer;
    pointer = node;
  }
  return pointer;
}

function toArray(list: ListNode | null) {
  if (!list) return [];
  const result: number[] = [];
  while (list) {
    result.push(list.val);
    list = list.next;
  }
  return result;
}
