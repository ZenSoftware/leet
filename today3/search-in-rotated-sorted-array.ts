/**
 * https://leetcode.com/problems/search-in-rotated-sorted-array/description/
 */
export { search };

function search(nums: number[], target: number): number {
  function search(start: number, end: number): number {
    const mid = Math.floor((start + end) / 2);
    if (target === nums[mid]) return mid;
    if (start >= end) return -1;

    if (nums[start] < nums[mid]) {
      // Left portion of rotation
      if (target < nums[start]) return search(mid + 1, end);
      else return search(start, mid - 1);
    } else {
      // Right portion of rotation
      if (target < nums[mid]) return search(start, mid - 1);
      else return search(mid + 1, end);
    }
  }

  return search(0, nums.length - 1);
}
