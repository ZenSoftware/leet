/**
 * https://leetcode.com/problems/jump-game/
 */

export function canJump(nums: number[]): boolean {
  function search(position: number): boolean {
    if (position >= nums.length - 1) return true;
    if (nums[position] === 0) return false;

    const steps = nums[position];
    for (let i = 1; i <= steps; i++) {
      const done = search(position + i);
      if (done) return true;
    }

    return false;
  }

  return search(0);
}
