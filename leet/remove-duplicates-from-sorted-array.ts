/**
 * https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
 */
export function removeDuplicates(nums: (number | null)[]): number {
  if (nums.length === 0) return 0;
  if (nums.length === 1) return 1;

  for (let i = 0; i < nums.length; i++) {
    let x = nums[i];
    let j = i + 1;
    while (nums[j] === x) {
      nums[j] = null;
      j++;
      i++;
    }
  }

  let i = 1;
  while (i < nums.length) {
    if (nums[i] === null) break;
    i++;
  }

  let j = i;
  while (j < nums.length) {
    if (nums[j] !== null) {
      nums[i] = nums[j];
      nums[j] = null;
      i++;
    }
    j++;
  }

  return i;
}
