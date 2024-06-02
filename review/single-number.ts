/**
 * https://leetcode.com/problems/single-number/description/
 * [NeetCode's solution](https://www.youtube.com/watch?v=qMPX1AOa83k)
 */
export { singleNumber };

function singleNumber(nums: number[]): number {
  return nums.reduce((prev, curr) => prev ^ curr);
}
