/**
 * https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
 * Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
 */

export { rotate };

function rotate(nums: number[], k: number): void {
  const result: number[] = [];
  let i = nums.length - (k % nums.length);
  while (result.length < nums.length) {
    if (i >= nums.length) i = 0;
    result.push(nums[i]);
    i++;
  }
  for (let i = 0; i < result.length; i++) {
    nums[i] = result[i];
  }
}
