/**
 * https://leetcode.com/problems/search-a-2d-matrix/description/
 */
export { searchMatrix, binarySearchRow, binarySearchCol };

function searchMatrix(matrix: number[][], target: number): boolean {
  const rowIndex = binarySearchCol(matrix, target);
  if (rowIndex === -1) return false;
  return binarySearchRow(matrix[rowIndex], target);
}

function binarySearchCol(matrix: number[][], target: number): number {
  const rowLastIndex = matrix.length - 1;

  for (let row = 0; row <= rowLastIndex - 1; row++) {
    if (matrix[row][0] <= target && target < matrix[row + 1][0]) return row;
  }

  return rowLastIndex;
}

function binarySearchRow(row: number[], target: number): boolean {
  function bs(start: number, end: number): boolean {
    if (row[start] === target) return true;
    if (row[end] === target) return true;
    if (start >= end) return false;

    const mid = Math.floor((start + end) / 2);

    if (target <= row[mid]) return bs(start, mid);
    else return bs(mid + 1, end);
  }

  return bs(0, row.length);
}
