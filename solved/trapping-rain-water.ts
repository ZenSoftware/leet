/**
 * https://leetcode.com/problems/trapping-rain-water/description/
 */
export function trap(height: number[]): number {
  const length = height.length;
  let maxL = Array(length);
  maxL[0] = 0;
  for (let i = 1; i < length; i++) {
    maxL[i] = Math.max(height[i - 1], maxL[i - 1]);
  }

  let maxR = Array(length);
  maxR[length - 1] = 0;
  for (let i = length - 2; i >= 0; i--) {
    maxR[i] = Math.max(height[i + 1], maxR[i + 1]);
  }

  let min = Array(length);
  for (let i = 0; i < length; i++) {
    min[i] = Math.min(maxL[i], maxR[i]);
  }

  let result = 0;
  for (let i = 0; i < length; i++) {
    let volume = min[i] - height[i];
    if (volume > 0) result += volume;
  }

  return result;
}
