/**
 * https://leetcode.com/problems/set-matrix-zeroes/description/
 */
export { setZeroes };

function setZeroes(matrix: number[][]): void {
  const rows = matrix.length;
  const cols = matrix[0].length;
  const zeros: ZeroCell[] = [];

  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      if (matrix[row][col] === 0) {
        zeros.push({ row, col });
      }
    }
  }

  for (let z = 0; z < zeros.length; z++) {
    setZero(matrix, zeros[z]);
  }
}

function setZero(matrix: number[][], zeroCell: ZeroCell): void {
  const rows = matrix.length;
  const cols = matrix[0].length;

  for (let col = 0; col < cols; col++) {
    matrix[zeroCell.row][col] = 0;
  }

  for (let row = 0; row < rows; row++) {
    matrix[row][zeroCell.col] = 0;
  }
}

interface ZeroCell {
  row: number;
  col: number;
}
