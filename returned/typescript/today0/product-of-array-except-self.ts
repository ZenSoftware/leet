/**
 * https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150
 * Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
 * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 * You must write an algorithm that runs in O(n) time and without using the division operation.
 */

export { productExceptSelf };

function productExceptSelf(nums: number[]): number[] {
  if (nums.length <= 1) return nums;

  // prefix pass
  const result = new Array(nums.length);
  result[0] = 1;
  for (let i = 1; i < nums.length; i++) {
    result[i] = result[i - 1] * nums[i - 1];
  }

  // postfix pass
  let postfix = 1;
  for (let i = nums.length - 2; i >= 0; i--) {
    postfix *= nums[i + 1];
    result[i] *= postfix;
  }

  return result;
}
