/**
 * https://leetcode.com/problems/maximum-product-subarray/
 */
export { maxProduct };

function maxProduct(nums: number[]): number {
  let max = -Infinity;

  for (let l = 0; l < nums.length; l++) {
    let product = 1;
    for (let r = l; r < nums.length; r++) {
      product *= nums[r];
      max = Math.max(max, product);
    }
  }

  return max;
}
