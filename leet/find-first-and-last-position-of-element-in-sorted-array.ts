/**
 * https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
 */

export function searchRange(nums: number[], target: number): number[] {
  return [];
}

export function binarySearch(nums: number[], find: number): number {
  function bs(start: number, end: number) {
    if (nums[start] === find) return start;
    if (nums[end] === find) return end;
    if (start >= end) return -1;

    const mid = Math.floor((start + end) / 2);

    if (find <= nums[mid]) return bs(start, mid);
    else return bs(mid + 1, end);
  }

  return bs(0, nums.length);
}
