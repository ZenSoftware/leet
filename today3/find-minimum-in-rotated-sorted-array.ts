/**
 * https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
 */
export { findMin };

function findMin(nums: number[]): number {
  function bs(start: number, end: number): number {
    if (start >= end) return nums[start];
  }
  return bs(0, nums.length - 1);
}
