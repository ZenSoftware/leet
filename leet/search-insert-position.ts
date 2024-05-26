/**
 * https://leetcode.com/problems/search-insert-position/description/
 */
export function searchInsert(nums: number[], target: number): number {
  return -2;
}

export function binarySearch(nums: number[], target: number): number {
  function bs(start: number, end: number): number {
    if (nums[start] === target) return start;
    if (nums[end] === target) return end;
    if (start >= end) return -1;

    const mid = Math.floor((start + end) / 2);

    if (target <= nums[mid]) return bs(start, mid);
    else return bs(mid + 1, end);
  }

  return bs(0, nums.length - 1);
}
