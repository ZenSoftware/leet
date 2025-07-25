import { ListNode, hasCycle } from './linked-list-cycle';

describe('Linked List Cycle', () => {
  it('evaluates correctly 1', () => {
    const l1 = new ListNode(1);
    const l2 = new ListNode(2);
    const l3 = new ListNode(3);
    const l4 = new ListNode(4);
    l1.next = l2;
    l2.next = l3;
    l3.next = l4;
    l4.next = l2;
    expect(hasCycle(l1)).toEqual(true);
  });

  it('evaluates correctly 2', () => {
    const l1 = new ListNode(1);
    const l2 = new ListNode(2);
    l1.next = l2;
    l2.next = l1;
    expect(hasCycle(l1)).toEqual(true);
  });

  it('evaluates correctly 3', () => {
    const l1 = new ListNode(1);
    expect(hasCycle(l1)).toEqual(false);
  });
});
