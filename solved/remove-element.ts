/**
 *
 */
export function removeElement(nums: number[], val: number): number {
  let i = 0;
  while (i < nums.length) {
    if (nums[i] === val) break;
    i++;
  }

  let j = i;
  while (j < nums.length) {
    if (nums[j] !== val) {
      nums[i] = nums[j];
      i++;
    }
    j++;
  }

  return i;
}
