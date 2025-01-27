/**
 * https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150
 * You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
 * Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
 * 0 <= j <= nums[i] and
 * i + j < n
 * Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
 */

export { jump };

function jump(nums: number[]): number {
  let l = 0;
  let r = 0;
  let result = 0;

  while (r < nums.length - 1) {
    let largest = 0;
    for (let i = l; i <= r; i++) {
      largest = Math.max(nums[i] + i, largest);
    }
    l = l + 1;
    r = largest;
    result++;
  }

  return result;
}
