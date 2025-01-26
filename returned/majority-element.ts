/**
 * https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
 * Given an array nums of size n, return the majority element.
 * The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
 */

export { majorityElement };

function majorityElement(nums: number[]): number {
  const majority_length = Math.floor(nums.length / 2);
  const hash: Record<number, number> = {};

  for (const num of nums) {
    let count = hash[num];
    if (count === undefined) count = 0;
    hash[num] = ++count;
    if (count > majority_length) return num;
  }

  throw 'No majority element';
}
