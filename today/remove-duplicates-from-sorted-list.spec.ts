import { deleteDuplicates, toArray, toList } from './remove-duplicates-from-sorted-list';

describe('Remove Duplicates from Sorted List', () => {
  it('evaluates correctly 1', () => {
    const input = toList([1, 1, 2]);
    const solution = deleteDuplicates(input);
    expect(toArray(solution)).toEqual([1, 2]);
  });

  it('evaluates correctly 2', () => {
    const input = toList([1, 1, 2, 3, 3]);
    const solution = deleteDuplicates(input);
    expect(toArray(solution)).toEqual([1, 2, 3]);
  });

  it('evaluates correctly 3', () => {
    const input = toList([1, 1]);
    const solution = deleteDuplicates(input);
    expect(toArray(solution)).toEqual([1]);
  });
});
