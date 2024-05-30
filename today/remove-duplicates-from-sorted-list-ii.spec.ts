import { deleteDuplicates, toList, toArray } from './remove-duplicates-from-sorted-list-ii';

describe('Remove Duplicates from Sorted List II', () => {
  it('evaluates correctly 1', () => {
    const input = toList([1, 2, 3, 3, 4, 4, 5]);
    const solution = deleteDuplicates(input);
    expect(toArray(solution)).toEqual([1, 2, 5]);
  });

  it('evaluates correctly 2', () => {
    const input = toList([1, 1, 1, 2, 3]);
    const solution = deleteDuplicates(input);
    expect(toArray(solution)).toEqual([2, 3]);
  });

  it('evaluates correctly 3', () => {
    const input = toList([1, 1]);
    const solution = deleteDuplicates(input);
    expect(toArray(solution)).toEqual([]);
  });

  it('constructs lists correctly', () => {
    const list = toList([1, 2, 3, 4]);
    const array = toArray(list);
    expect(array).toEqual([1, 2, 3, 4]);
  });
});
