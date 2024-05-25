import { mergeTwoLists, toArray, toList } from './merge-two-sorted-lists';

describe('Merge Two Sorted Lists', () => {
  it('evaluates correctly', () => {
    expect(false).toEqual(true);
  });

  it('constructs lists correctly', () => {
    const list = toList([1, 2, 3, 4]);
    const array = toArray(list);
    expect(array).toEqual([1, 2, 3, 4]);
  });
});
