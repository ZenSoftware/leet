/**
 * https://leetcode.com/problems/jump-game-ii/
 */
export function jump(nums: number[]): number {
  let count = 0;
  let i = 0;
  while (i < nums.length - 1) {
    let steps = nums[i];
    let candidateMax = 0;
    let bestIndex = 0;
    for (let j = 0; j < steps; j++) {
      const candidateIndex = i + steps - j;
      const candidateMove = candidateIndex + nums[candidateIndex];
      if (candidateMove > candidateMax) {
        candidateMax = candidateMove;
        bestIndex = candidateIndex;
      }
      if (bestIndex >= nums.length - 1) return count + 1;
    }
    i = bestIndex;
    count++;
  }
  return count;
}
