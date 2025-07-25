/**
 * https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
 */
export { removeDuplicates };

function removeDuplicates(nums: number[]): number {
  if (nums.length === 1) return 1;

  // Replace all values with duplicates greater than 2 with null
  let lastUnique = nums[0];
  let duplicateCount = 1;
  for (let i = 1; i < nums.length; i++) {
    if (lastUnique === nums[i]) {
      duplicateCount++;
    } else {
      duplicateCount = 1;
      lastUnique = nums[i];
    }

    if (duplicateCount > 2) {
      nums[i] = null as any;
    }
  }

  // Initialize first null position
  let i = 0;
  while (i < nums.length) {
    if (nums[i] === null) {
      break;
    }
    i++;
  }

  // Shuffle all none null values backwards
  let j = i + 1;
  while (j < nums.length) {
    if (nums[j] !== null) {
      nums[i] = nums[j];
      i++;
    }
    j++;
  }

  return i;
}
