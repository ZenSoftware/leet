/**
 * https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
 */
export { removeDuplicates };

function removeDuplicates(nums: number[]): number {
  if (nums.length === 0) return 1;

  let duplicateCount = 0;
  for (let i = 1; i < nums.length; i++) {
    if (nums[i - 1] === nums[i]) duplicateCount++;
    if (duplicateCount === 2) {
      console.log();
    }
  }

  return -1;
}
