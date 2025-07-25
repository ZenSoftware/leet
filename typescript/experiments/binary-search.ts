export function binarySearch(nums: number[], target: number) {
  function bs(start: number, end: number): number {
    const mid = Math.floor((start + end) / 2);
    if (target === nums[mid]) return mid;
    if (start >= end) return -1;
    if (target < nums[mid]) return bs(start, mid - 1);
    else return bs(mid + 1, end);
  }
  return bs(0, nums.length - 1);
}
