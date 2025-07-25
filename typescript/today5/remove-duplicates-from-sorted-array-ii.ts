/**
 * https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
 * Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
 * Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
 * Return k after placing the final result in the first k slots of nums.
 * Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
 */

export { removeDuplicates };

function removeDuplicates(nums: number[]): number {
  let index = 1;
  let i = 1;
  let dupCount = 0;

  while (i < nums.length) {
    if (nums[i - 1] === nums[i]) {
      if (dupCount < 1) {
        nums[index++] = nums[i++];
      } else {
        i++;
      }
      dupCount++;
    } else {
      dupCount = 0;
      nums[index++] = nums[i++];
    }
  }

  return index;
}
