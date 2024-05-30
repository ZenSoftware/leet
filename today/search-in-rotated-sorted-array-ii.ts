/**
 * https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
 * [NeetCode Solution](https://www.youtube.com/watch?v=oUnF7o88_Xc&t=359s)
 */
export { search, binarySearch };

function search(nums: number[], target: number): boolean {
  return false;
}

function binarySearch(nums: number[], target: number): number {
  function bs(start: number, end: number) {
    const mid = Math.floor((start + end) / 2);
    if (nums[mid] === target) return mid;
    if (start >= end) return -1;

    if (nums[start] < nums[mid]) {
      // in left rotation
    } else {
      // in right rotation
    }

    if (target <= nums[mid]) return bs(start, mid);
    else return bs(mid + 1, end);
  }

  return bs(0, nums.length - 1);
}
