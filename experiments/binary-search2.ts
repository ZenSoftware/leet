export { binarySearch };

function binarySearch(nums: number[], target: number): number {
  function bs(start: number, end: number): number {
    const mid = Math.floor((start + end) / 2);
    if (nums[mid] === target) return mid;
    if (start >= end) return -1;
    if (target <= nums[mid]) return bs(start, mid);
    else return bs(mid + 1, end);
  }
  return bs(0, nums.length - 1);
}
