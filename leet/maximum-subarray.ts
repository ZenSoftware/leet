/**
 * https://leetcode.com/problems/maximum-subarray/
 */
export function maxSubArray(nums: number[]): number {
  let largest = -Infinity;
  for (let i = 0; i < nums.length; i++) {
    for (let j = i; j < nums.length; j++) {
      let sum = 0;
      for (let k = i; k <= j; k++) {
        sum += nums[k];
      }
      if (sum > largest) largest = sum;
    }
  }
  return largest;
}
