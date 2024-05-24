/**
 * https://leetcode.com/problems/3sum/description/
 */
export function threeSum(nums: number[]): number[][] {
  let results: number[][] = [];

  for (let i = 0; i < nums.length - 2; i++) {
    for (let j = i + 1; j < nums.length - 1; j++) {
      for (let k = j + 1; k < nums.length; k++) {
        if (nums[i] + nums[j] + nums[k] === 0) {
          const solution = [nums[i], nums[j], nums[k]];
          solution.sort((a, b) => a - b);
          if (!contains(results, solution)) {
            results.push(solution);
          }
        }
      }
    }
  }

  return results;
}

function contains(result: number[][], solution: number[]): boolean {
  for (let r of result) {
    let contains = false;
    for (let i = 0; i < 3; i++) {
      if (r[i] !== solution[i]) break;
      if (i === 2 && r[i] === solution[i]) return true;
    }
  }
  return false;
}
