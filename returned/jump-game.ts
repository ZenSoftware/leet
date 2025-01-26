/**
 * https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150
 * You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
 * Return true if you can reach the last index, or false otherwise.
 */

export { canJump };

function canJump(nums: number[]): boolean {
  let goal = nums.length - 2;

  for (let i = nums.length - 1; i >= 0; i--) {
    if (i + nums[i] >= goal) {
      goal = i;
    }
  }

  return goal === 0;
}
