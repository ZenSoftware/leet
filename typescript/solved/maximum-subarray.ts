/**
 * https://leetcode.com/problems/maximum-subarray/
 */
export function maxSubArray(nums: number[]): number {
  let largest = -Infinity;
  let sum = 0;
  for (let i = 0; i < nums.length; i++) {
    if (sum < 0) sum = 0;
    sum += nums[i];
    largest = Math.max(largest, sum);
  }
  return largest;
}
