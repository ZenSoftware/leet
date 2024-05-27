/**
 * https://leetcode.com/problems/jump-game-ii/
 */
export function jump(nums: number[]): number {
  let count = 0;
  let i = 0;
  while (i < nums.length - 1) {
    let steps = nums[i];
    let candidateMax = 0;
    let candidateIndex = 0;
    for (let j = 0; j < steps; j++) {
      const nextIndex = i + steps - j;
      const candidateMove = nextIndex + nums[nextIndex];
      if (candidateMove > candidateMax) {
        candidateMax = candidateMove;
        candidateIndex = nextIndex;
      }
      if (candidateIndex >= nums.length - 1) return count + 1;
    }
    i = candidateIndex;
    count++;
  }
  return count;
}
