/**
 * https://leetcode.com/problems/maximum-product-subarray/
 */
export { maxProduct };

function maxProduct(nums: number[]): number {
  let max = nums.reduce((accum, curr) => Math.max(accum, curr));
  let curMin = 1;
  let curMax = 1;

  for (const n of nums) {
    if (n === 0) {
      curMin = 1;
      curMax = 1;
    }

    const tmp = curMax * n;
    curMax = Math.max(curMin * n, curMax * n, n);
    curMin = Math.min(curMin * n, tmp, n);
    max = Math.max(max, curMax);
  }

  return max;
}
