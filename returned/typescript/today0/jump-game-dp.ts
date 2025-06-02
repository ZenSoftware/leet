/**
 * https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150
 * You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
 * Return true if you can reach the last index, or false otherwise.
 */

export { canJump };

function canJump(nums: number[]): boolean {
  const cache = new Map<number, boolean>();

  function jump(index: number): boolean {
    if (index >= nums.length - 1) return true;
    if (nums[index] === 0) return false;
    if (cache.has(index)) return cache.get(index) as boolean;

    for (let i = nums[index]; i >= 1; i--) {
      if (jump(index + i)) {
        cache.set(index, true);
        return true;
      }
    }

    cache.set(index, false);
    return false;
  }

  return jump(0);
}
