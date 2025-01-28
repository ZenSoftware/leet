/**
 * https://leetcode.com/problems/trapping-rain-water/?envType=study-plan-v2&envId=top-interview-150
 * Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
 */

export { trap };

function trap(height: number[]): number {
  let l = 0;
  let r = height.length - 1;
  let maxL = height[l];
  let maxR = height[r];
  let total = 0;

  while (l < r) {
    let trapped = 0;
    if (maxL <= maxR) {
      l++;
      trapped = maxL - height[l];
      maxL = Math.max(maxL, height[l]);
    } else {
      r--;
      trapped = maxR - height[r];
      maxR = Math.max(maxR, height[r]);
    }
    total += Math.max(0, trapped);
  }

  return total;
}
