/**
 * https://leetcode.com/problems/search-insert-position/description/
 */
export function searchInsert(nums: number[], target: number): number {
  function bs(start: number, end: number): number {
    if (nums[start] === target) return start;
    if (nums[end] === target) return end;
    if (start >= end) {
      if (target < nums[start]) return start;
      else return start + 1;
    }

    const mid = Math.floor((start + end) / 2);

    if (target <= nums[mid]) return bs(start, mid);
    else return bs(mid + 1, end);
  }

  return bs(0, nums.length - 1);
}
