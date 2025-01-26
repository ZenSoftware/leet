import { removeDuplicates } from './remove-duplicates-from-sorted-array';

describe('Remove Duplicates from Sorted Array', () => {
  it('evaluates correctly', () => {
    let nums = [1, 1, 2];
    let k = removeDuplicates(nums);
    expect(nums).toEqual([1, 2, 2]);
    expect(k).toEqual(2);
  });
});
