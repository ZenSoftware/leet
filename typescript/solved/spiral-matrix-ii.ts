/**
 * https://leetcode.com/problems/spiral-matrix-ii/
 */

export function generateMatrix(n: number): number[][] {
  let result: number[][] = Array(n);
  for (let i = 0; i < n; i++) {
    result[i] = Array(n);
  }

  let top = 0;
  let bottom = n - 1;
  let left = 0;
  let right = n - 1;
  let cellCount = n * n;
  let count = 1;

  while (count <= cellCount) {
    // Traverse right
    for (let i = left; i <= right; i++) {
      result[top][i] = count;
      count++;
    }
    if (count > cellCount) return result;
    top++;

    // Traverse down
    for (let i = top; i <= bottom; i++) {
      result[i][right] = count;
      count++;
    }
    if (count > cellCount) return result;
    right--;

    // Traverse left
    for (let i = right; i >= left; i--) {
      result[bottom][i] = count;
      count++;
    }
    if (count > cellCount) return result;
    bottom--;

    // Traverse up
    for (let i = bottom; i >= top; i--) {
      result[i][left] = count;
      count++;
    }
    left++;
  }

  return result;
}
