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

  function bs(start: number, end: number): number {
    if (matrix[start][0] === target) return start;
    if (matrix[end][0] === target) return end;
    if (start >= end) {
      if (start === 0) {
        if (target < matrix[start][0]) return -1;
        else return 0;
      }
      if (matrix[start - 1][0] <= target && target < matrix[start][0]) return start - 1;
      if (start === rowLastIndex) return rowLastIndex;
      if (matrix[start][0] <= target && target < matrix[start + 1][0]) return start;
      return start + 1;
    }

    const mid = Math.floor((start + end) / 2);

    if (target <= matrix[mid][0]) return bs(start, mid);
    else return bs(mid + 1, end);
  }

  return bs(0, rowLastIndex);
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
