/**
 * https://leetcode.com/problems/3sum/description/
 */
export function threeSum(nums: number[]): number[][] {
  let results: number[][] = [];
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    for (let j = i + 1; j < nums.length - 1; j++) {
      for (let k = j + 1; k < nums.length; k++) {
        if (nums[i] + nums[j] + nums[k] === 0) {
        }
      }
    }
  }

  return results;
}

export function binarySearch(nums: number[], find: number) {
  function bs(start: number, end: number) {
    if (nums[start] === find) return start;
    if (nums[end] === find) return end;
    if (start >= end) return -1;

    const mid = Math.floor((start + end) / 2);

    if (find <= nums[mid]) return bs(start, mid);
    else return bs(mid + 1, end);
  }

  return bs(0, nums.length - 1);
}
