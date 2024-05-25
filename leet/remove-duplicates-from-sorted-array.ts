/**
 * https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
 */
export function removeDuplicates(nums: number[]): number {
  if (nums.length === 0) return 0;
  if (nums.length === 1) return 1;

  for (let i = 0; i < nums.length - 1; i++) {
    let j = i;

    while (nums[j] === nums[j + 1]) {
      j++;

      const temp = nums[j];

      for (let k = j; k < nums.length - 1; k++) {
        nums[k] = nums[k + 1];
      }

      nums[nums.length - 1] = temp;
    }

    if (nums[i] > nums[i + 1]) break;
  }

  let k = 1;
  for (let i = 0; i < nums.length - 1; i++) {
    if (nums[i] >= nums[i + 1]) break;
    k++;
  }

  return k;
}
