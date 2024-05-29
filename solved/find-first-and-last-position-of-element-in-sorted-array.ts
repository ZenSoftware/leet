/**
 * https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
 */

export function searchRange(nums: number[], target: number): number[] {
  const foundIndex = binarySearch(nums, target);
  if (foundIndex === -1) return [-1, -1];

  let foundStart = foundIndex;
  while (nums[foundStart] === nums[foundStart - 1]) {
    foundStart--;
  }

  let foundEnd = foundIndex;
  while (nums[foundEnd] === nums[foundEnd + 1]) {
    foundEnd++;
  }

  return [foundStart, foundEnd];
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
