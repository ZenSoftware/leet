import { mergeKLists, mergeLists, toArray, toList } from './merge-k-sorted-lists';

describe('Merge k Sorted Lists', () => {
  it('evaluates correctly 1', () => {
    const l1 = toList([1, 4, 5]);
    const l2 = toList([1, 3, 4]);
    const l3 = toList([2, 6]);
    const result = mergeKLists([l1, l2, l3]);
    expect(toArray(result)).toEqual([1, 1, 2, 3, 4, 4, 5, 6]);
  });

  it('evaluates mergeLists correctly', () => {
    const l1 = toList([1, 2, 3]);
    const l2 = toList([1, 3, 4]);
    const result = mergeLists(l1, l2);
    expect(toArray(result)).toEqual([1, 1, 2, 3, 3, 4]);
  });

  it('constructs lists correctly', () => {
    const list = toList([1, 2, 3, 4]);
    const array = toArray(list);
    expect(array).toEqual([1, 2, 3, 4]);
  });
});
