/**
 * https://leetcode.com/problems/spiral-matrix/
 */
export function spiralOrder(matrix: number[][]): number[] {
  let topBound = 0;
  let bottomBound = matrix.length - 1;
  let leftBound = 0;
  let rightBound = matrix[0].length - 1;

  const cellCount = matrix.length * matrix[0].length;
  const result: number[] = [];

  while (result.length < cellCount) {
    // Traverse right
    for (let i = leftBound; i <= rightBound; i++) {
      result.push(matrix[topBound][i]);
    }
    if (result.length >= cellCount) return result;
    topBound++;

    // Traverse down
    for (let i = topBound; i <= bottomBound; i++) {
      result.push(matrix[i][rightBound]);
    }
    if (result.length >= cellCount) return result;
    rightBound--;

    // Traverse left
    for (let i = rightBound; i >= leftBound; i--) {
      result.push(matrix[bottomBound][i]);
    }
    if (result.length >= cellCount) return result;
    bottomBound--;

    // Traverse up
    for (let i = bottomBound; i >= topBound; i--) {
      result.push(matrix[i][leftBound]);
    }
    leftBound++;
  }

  return result;
}
