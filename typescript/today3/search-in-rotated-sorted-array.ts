/**
 * https://leetcode.com/problems/search-in-rotated-sorted-array/description/
 */
export { search };

function search(nums: number[], target: number): number {
  function bs(start: number, end: number): number {
    const mid = Math.floor((start + end) / 2);
    if (target === nums[mid]) return mid;
    if (start >= end) return -1;

    if (nums[start] <= nums[mid]) {
      // Left portion of rotation
      if (target > nums[mid]) {
        return bs(mid + 1, end);
      } else {
        if (target >= nums[start]) return bs(start, mid - 1);
        else return bs(mid + 1, end);
      }
    } else {
      // Right portion of rotation
      if (target < nums[mid]) {
        return bs(start, mid - 1);
      } else {
        if (target <= nums[end]) return bs(mid + 1, end);
        return bs(start, mid - 1);
      }
    }
  }

  return bs(0, nums.length - 1);
}
