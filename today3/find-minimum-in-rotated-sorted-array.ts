/**
 * https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
 */
export { findMin };

function findMin(nums: number[]): number {
  function bs(start: number, end: number): number {
    if (start >= end) return nums[start];

    const mid = Math.floor((start + end) / 2);
    if (nums[start] <= nums[mid]) {
      // Left portion of rotation
    } else {
      // Right portion of rotation
    }
  }
  return bs(0, nums.length - 1);
}
