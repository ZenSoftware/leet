/**
 * https://leetcode.com/problems/sudoku-solver/description/
 */
export function solveSudoku(board: string[][]): void {
  const unused2x2 = init(board);
}

export function init(board: string[][]): (Set<string> | null)[][] {
  // Count the number of used values for each 3x3 subsection's
  const subSectionUsed: Set<string>[][] = Array(3);
  for (let sectionRow = 0; sectionRow <= 2; sectionRow++) {
    subSectionUsed[sectionRow] = Array(3);
    for (let sectionCol = 0; sectionCol <= 2; sectionCol++) {
      subSectionUsed[sectionRow][sectionCol] = new Set();
      const rowOffset = sectionRow * 3;
      for (let row = 0 + rowOffset; row <= 2 + rowOffset; row++) {
        const colOffset = sectionCol * 3;
        for (let col = 0 + colOffset; col <= 2 + colOffset; col++) {
          const val = board[row][col];
          if (val !== '.') {
            subSectionUsed[sectionRow][sectionCol].add(val);
          }
        }
      }
    }
  }

  // Count the number of used values for each individual cell
  const unused: Set<string>[][] = new Array(9);
  for (let row = 0; row < 9; row++) {
    unused[row] = Array(9).fill(null);
  }

  for (let sectionRow = 0; sectionRow <= 2; sectionRow++) {
    for (let sectionCol = 0; sectionCol <= 2; sectionCol++) {
      const rowOffset = sectionRow * 3;
      for (let row = 0 + rowOffset; row <= 2 + rowOffset; row++) {
        const colOffset = sectionCol * 3;
        for (let col = 0 + colOffset; col <= 2 + colOffset; col++) {
          const val = board[row][col];
          if (val === '.') {
            unused[row][col] = new Set(['1', '2', '3', '4', '5', '6', '7', '8', '9']);
            for (let usedVal of subSectionUsed[sectionRow][sectionCol]) {
              unused[row][col].delete(usedVal);
            }

            for (let i = 0; i < 9; i++) {
              if (board[i][col] !== '.' && !(rowOffset <= i && i <= rowOffset + 2)) {
                unused[row][col].delete(board[i][col]);
              }
            }

            for (let j = 0; j < 9; j++) {
              if (board[row][j] !== '.' && !(colOffset <= j && j <= colOffset + 2)) {
                unused[row][col].delete(board[row][j]);
              }
            }
          }
        }
      }
    }
  }

  return unused;
}
