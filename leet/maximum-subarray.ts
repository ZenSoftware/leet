/**
 * https://leetcode.com/problems/maximum-subarray/
 */
export function maxSubArray(nums: number[]): number {
  let largest = -Infinity;
  for (let i = 0; i < nums.length; i++) {
    let sum = 0;
    for (let j = i; j < nums.length; j++) {
      sum += nums[j];
      if (sum > largest) largest = sum;
    }
  }
  return largest;
}
