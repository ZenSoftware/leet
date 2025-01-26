import { removeDuplicates } from './remove-duplicates-from-sorted-array-ii';

describe('Remove Duplicates from Sorted Array II', () => {
  it('evaluates correctly 1', () => {
    let nums = [1, 1, 1, 2, 2, 3];
    let k = removeDuplicates(nums);
    expect(nums).toEqual([1, 1, 2, 2, 3, 3]);
    expect(k).toEqual(5);
  });

  it('evaluates correctly 2', () => {
    let nums = [0, 0, 1, 1, 1, 1, 2, 3, 3];
    let k = removeDuplicates(nums);
    expect(nums).toEqual([0, 0, 1, 1, 2, 3, 3, 3, 3]);
    expect(k).toEqual(7);
  });
});
