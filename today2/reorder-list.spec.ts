import { reorderList, toArray, toList, ListNode } from './reorder-list';

describe('Reorder List', () => {
  it('evaluates correctly 1', () => {
    const input = toList([1, 2, 3, 4]);
    reorderList(input);
    expect(toArray(input)).toEqual([1, 4, 2, 3]);
  });

  it('evaluates correctly 2', () => {
    const input = toList([1, 2, 3, 4, 5]);
    reorderList(input);
    expect(toArray(input)).toEqual([1, 5, 2, 4, 3]);
  });

  it('constructs lists correctly', () => {
    const list = toList([1, 2, 3, 4]);
    const array = toArray(list);
    expect(array).toEqual([1, 2, 3, 4]);
  });
});
