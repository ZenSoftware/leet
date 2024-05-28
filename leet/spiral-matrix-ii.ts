/**
 * https://leetcode.com/problems/spiral-matrix-ii/
 */

export function generateMatrix(n: number): number[][] {
  let top = 0;
  let bottom = n - 1;
  let left = 0;
  let right = n - 1;

  let result: number[][] = Array(n);
  for (let i = 0; i < n; i++) {
    result[i] = Array(n);
  }

  return result;
}
