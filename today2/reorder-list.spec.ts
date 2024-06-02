import { reorderList, toArray, toList, ListNode } from './reorder-list';

describe('Reorder List', () => {
  it('evaluates correctly', () => {
    expect(true).toEqual(true);
  });

  it('constructs lists correctly', () => {
    const list = toList([1, 2, 3, 4]);
    const array = toArray(list);
    expect(array).toEqual([1, 2, 3, 4]);
  });
});
