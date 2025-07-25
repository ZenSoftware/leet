/**
 * https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
 */
export function twoSum(numbers: number[], target: number): number[] {
  let l = 0;
  let r = numbers.length - 1;

  while (l < r) {
    let sum = numbers[l] + numbers[r];
    if (sum === target) return [l + 1, r + 1];
    else if (sum > target) r--;
    else l++;
  }

  throw Error('No solution exists');
}
