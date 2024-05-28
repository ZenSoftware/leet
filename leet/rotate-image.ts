/**
 * https://leetcode.com/problems/rotate-image/description/
 */

export function rotate(matrix: number[][]): void {
  transpose(matrix);
  swap(matrix);
}

export function transpose(matrix: number[][]): void {
  const size = matrix.length;
  for (let i = 0; i < size; i++) {
    for (let j = i + 1; j < size; j++) {
      const temp = matrix[i][j];
      matrix[i][j] = matrix[j][i];
      matrix[j][i] = temp;
    }
  }
}

export function swap(matrix: number[][]): void {
  const size = matrix.length;
  const half = Math.floor(size / 2);
  for (let j = 0; j < half; j++) {
    for (let i = 0; i < size; i++) {
      const temp = matrix[i][j];
      matrix[i][j] = matrix[i][size - j - 1];
      matrix[i][size - j - 1] = temp;
    }
  }
}
