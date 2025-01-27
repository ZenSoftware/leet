/**
 * https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150
 * Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
 * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 * You must write an algorithm that runs in O(n) time and without using the division operation.
 */

export { productExceptSelf };

function productExceptSelf(nums: number[]): number[] {
  if (nums.length <= 1) return nums;

  const prefix = new Array(nums.length);
  prefix[0] = nums[0];
  for (let i = 1; i < prefix.length; i++) {
    prefix[i] = prefix[i - 1] * nums[i];
  }

  const postfix = new Array(nums.length);
  postfix[postfix.length - 1] = nums[nums.length - 1];
  for (let i = postfix.length - 2; i >= 0; i--) {
    postfix[i] = nums[i] * postfix[i + 1];
  }

  const result = new Array(nums.length);
  result[0] = postfix[1];
  result[result.length - 1] = prefix[prefix.length - 2];
  for (let i = 1; i <= result.length - 2; i++) {
    result[i] = prefix[i - 1] * postfix[i + 1];
  }

  return result;
}
