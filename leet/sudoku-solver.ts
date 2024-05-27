/**
 * https://leetcode.com/problems/sudoku-solver/description/
 */
export function solveSudoku(board: string[][]): void {
  const usedTotals = init(board);
}

export function init(board: string[][]): number[][] {
  // Count the number of used values for each 3x3 subsection's
  const subSectionTotals: number[][] = new Array(3);
  for (let sectionRow = 0; sectionRow <= 2; sectionRow++) {
    subSectionTotals[sectionRow] = Array(3).fill(0);
    for (let sectionCol = 0; sectionCol <= 2; sectionCol++) {
      const rowOffset = sectionRow * 3;
      for (let row = 0 + rowOffset; row <= 2 + rowOffset; row++) {
        const colOffset = sectionCol * 3;
        for (let col = 0 + colOffset; col <= 2 + colOffset; col++) {
          const val = board[row][col];
          if (val !== '.') {
            subSectionTotals[sectionRow][sectionCol]++;
          }
        }
      }
    }
  }

  // Count the number of used values for each individual cell
  const individualCellTotals: number[][] = new Array(9);
  for (let row = 0; row < 9; row++) {
    individualCellTotals[row] = Array(9).fill(null);
  }

  for (let sectionRow = 0; sectionRow <= 2; sectionRow++) {
    for (let sectionCol = 0; sectionCol <= 2; sectionCol++) {
      const rowOffset = sectionRow * 3;
      for (let row = 0 + rowOffset; row <= 2 + rowOffset; row++) {
        const colOffset = sectionCol * 3;
        for (let col = 0 + colOffset; col <= 2 + colOffset; col++) {
          const val = board[row][col];
          if (val === '.') {
            individualCellTotals[row][col] = subSectionTotals[sectionRow][sectionCol];

            for (let i = 0; i < 9; i++) {
              if (board[i][col] !== '.' && !(rowOffset <= i && i <= rowOffset + 2)) {
                individualCellTotals[row][col]++;
              }
            }

            for (let j = 0; j < 9; j++) {
              if (board[row][j] !== '.' && !(colOffset <= j && j <= colOffset + 2)) {
                individualCellTotals[row][col]++;
              }
            }
          }
        }
      }
    }
  }

  return individualCellTotals;
}
