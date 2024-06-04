/**
 * https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
 * [NeetCode Solution](https://www.youtube.com/watch?v=oUnF7o88_Xc&t=359s)
 */
export { search };

function search(nums: number[], target: number): boolean {
  function bs(start: number, end: number): boolean {
    const mid = Math.floor((start + end) / 2);
    if (nums[mid] === target) return true;
    if (start >= end) return false;

    if (nums[start] <= nums[mid]) {
      // in left rotation
      if (target > nums[mid]) {
        return bs(mid + 1, end);
      } else {
        if (target >= nums[start]) return bs(start, mid - 1);
        else return bs(mid + 1, end);
      }
    } else {
      // in right rotation
      if (target < nums[mid]) {
        return bs(start, mid - 1);
      } else {
        if (target <= nums[end]) return bs(mid + 1, end);
        else return bs(start, mid - 1);
      }
    }
  }

  return bs(0, nums.length - 1);
}
