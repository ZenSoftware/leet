/**
 * https://leetcode.com/problems/two-sum/description/
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * You can return the answer in any order.
 * 2 <= nums.length <= 10^4
 * -10^9 <= nums[i] <= 10^9
 * -10^9 <= target <= 10^9
 */
export function twoSum(nums: number[], target: number): number[] {
  const cache: Record<string, number> = {};

  for (let i = 0; i < nums.length; i++) {
    const dif = target - nums[i];
    if (cache[dif] !== undefined) return [cache[dif], i];
    else cache[nums[i]] = i;
  }

  return [];
}
