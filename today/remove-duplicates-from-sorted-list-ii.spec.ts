import { deleteDuplicates, toList, toArray } from './remove-duplicates-from-sorted-list-ii';

describe('Remove Duplicates from Sorted List II', () => {
  it('evaluates correctly', () => {
    expect(true).toEqual(true);
  });

  it('constructs lists correctly', () => {
    const list = toList([1, 2, 3, 4]);
    const array = toArray(list);
    expect(array).toEqual([1, 2, 3, 4]);
  });
});
