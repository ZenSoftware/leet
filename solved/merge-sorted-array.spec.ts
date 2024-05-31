import { merge } from './merge-sorted-array';

describe('Merge Sorted Array', () => {
  it('evaluates correctly 1', () => {
    let nums1 = [1, 2, 3, 0, 0, 0];
    let nums2 = [2, 5, 6];
    merge(nums1, 3, nums2, 3);
    expect(nums1).toEqual([1, 2, 2, 3, 5, 6]);
  });

  it('evaluates correctly 2', () => {
    let nums1 = [1];
    let nums2 = [] as number[];
    merge(nums1, 1, nums2, 0);
    expect(nums1).toEqual([1]);
  });

  it('evaluates correctly 3', () => {
    let nums1 = [0];
    let nums2 = [1] as number[];
    merge(nums1, 0, nums2, 1);
    expect(nums1).toEqual([1]);
  });
});
