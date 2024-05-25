/**
 * https://leetcode.com/problems/3sum/description/
 */
export function threeSum(nums: number[]): number[][] {
  let results: number[][] = [];
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    if (nums[i] === nums[i - 1]) continue;

    let left = i + 1;
    let right = nums.length - 1;
    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];
      if (sum === 0) {
        results.push([nums[i], nums[left], nums[right]]);
        left++;
        right--;
        while (nums[left] === nums[left + 1] && left < right) left++;
      } else if (sum < 0) {
        left++;
      } else {
        right--;
      }
    }
  }

  return results;
}
