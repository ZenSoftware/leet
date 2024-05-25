import { mergeTwoLists, toArray, toList } from './merge-two-sorted-lists';

describe('Merge Two Sorted Lists', () => {
  it('evaluates correctly 1', () => {
    const list1 = toList([1, 2, 4]);
    const list2 = toList([1, 3, 4]);
    const result = mergeTwoLists(list1, list2);
    expect(toArray(result)).toEqual([1, 1, 2, 3, 4]);
  });

  it('evaluates correctly 2', () => {
    const list1 = toList([]);
    const list2 = toList([]);
    const result = mergeTwoLists(list1, list2);
    expect(toArray(result)).toEqual([]);
  });

  it('evaluates correctly 3', () => {
    const list1 = toList([]);
    const list2 = toList([0]);
    const result = mergeTwoLists(list1, list2);
    expect(toArray(result)).toEqual([0]);
  });

  it('constructs lists correctly', () => {
    const list = toList([1, 2, 3, 4]);
    const array = toArray(list);
    expect(array).toEqual([1, 2, 3, 4]);
  });
});
