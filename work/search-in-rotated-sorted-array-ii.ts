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
    } else {
      // in right rotation
    }
  }

  return bs(0, nums.length - 1);
}
