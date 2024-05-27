/**
 * https://leetcode.com/problems/rotate-image/description/
 */

export function rotate(matrix: number[][]): void {
  // Transpose
  [matrix[0][1], matrix[1][0]] = [matrix[1][0], matrix[0][1]];
  [matrix[0][2], matrix[2][0]] = [matrix[2][0], matrix[0][2]];
  [matrix[1][2], matrix[2][1]] = [matrix[2][1], matrix[1][2]];

  // Swap columns
  [matrix[0][0], matrix[0][2]] = [matrix[0][2], matrix[0][0]];
  [matrix[1][0], matrix[1][2]] = [matrix[1][2], matrix[1][0]];
  [matrix[2][0], matrix[2][2]] = [matrix[2][2], matrix[2][0]];
}
