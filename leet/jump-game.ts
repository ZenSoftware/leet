/**
 * https://leetcode.com/problems/jump-game/
 */

export function canJump(nums: number[]): boolean {
  const memo = new Set<number>();

  function search(position: number): boolean {
    if (memo.has(position)) return false;

    if (position >= nums.length - 1) return true;

    if (nums[position] === 0) {
      memo.add(position);
      return false;
    }

    const steps = nums[position];
    for (let i = steps; i > 0; i--) {
      const done = search(position + i);
      if (done) return true;
    }

    memo.add(position);
    return false;
  }

  return search(0);
}
