/**
 * https://leetcode.com/problems/first-missing-positive/
 */
export function firstMissingPositive(nums: number[]): number {
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] <= 0) {
      nums[i] = nums.length + 1;
    }
  }

  for (let i = 0; i < nums.length; i++) {
    const absNum = Math.abs(nums[i]);
    if (absNum <= nums.length && nums[absNum - 1] > 0) {
      nums[absNum - 1] *= -1;
    }
  }

  for (let c = 1; c <= nums.length; c++) {
    if (nums[c - 1] > 0) {
      return c;
    }
  }

  return nums.length + 1;
}
