/**
 * https://leetcode.com/problems/jump-game-ii/
 */
export function jump(nums: number[]): number {
  let count = 0;
  let i = 0;

  while (i < nums.length - 1) {
    let steps = nums[i];

    for (let j = 0; j < steps; j++) {
      const forwardIndex = i + steps - j;
      if (forwardIndex >= nums.length - 1 || nums[forwardIndex] > 0) {
        i = forwardIndex;
        count++;
        break;
      }
    }
  }

  return count;
}
