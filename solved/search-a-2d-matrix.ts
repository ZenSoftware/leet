/**
 * https://leetcode.com/problems/search-a-2d-matrix/description/
 */
export { searchMatrix, binarySearchRow };

function searchMatrix(matrix: number[][], target: number): boolean {
  const rowLastIndex = matrix.length - 1;
  const colLastIndex = matrix[0].length - 1;

  return false;
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
