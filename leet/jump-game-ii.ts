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
      const forwardIndex = i + steps - j;
      const candidateMove = forwardIndex + nums[forwardIndex];
      if (candidateMove > candidateMax) {
        candidateMax = candidateMove;
        candidateIndex = forwardIndex;
      }
      if (candidateIndex >= nums.length - 1) return count + 1;
    }
    i = candidateIndex;
    count++;
  }
  return count;
}
