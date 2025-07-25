import { ListNode, detectCycle } from './linked-list-cycle-ii';

describe('Linked List Cycle II', () => {
  it('evaluates correctly', () => {
    const l1 = new ListNode(1);
    const l2 = new ListNode(2);
    const l3 = new ListNode(3);
    const l4 = new ListNode(4);
    l1.next = l2;
    l2.next = l3;
    l3.next = l4;
    l4.next = l2;
    expect(detectCycle(l1)).toEqual(l2);
  });
});
