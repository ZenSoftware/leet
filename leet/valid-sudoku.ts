/**
 * https://leetcode.com/problems/valid-sudoku/description/
 */
export function isValidSudoku(board: string[][]): boolean {
  return rowsValid(board) && columnsValid(board) && threeByThreeValid(board);
}

export function rowsValid(board: string[][]): boolean {
  for (let row = 0; row < 9; row++) {
    const set = new Set<string>();
    for (let col = 0; col < 9; col++) {
      const val = board[row][col];
      if (val !== '.') {
        if (set.has(val)) return false;
        else set.add(val);
      }
    }
  }

  return true;
}

export function columnsValid(board: string[][]): boolean {
  for (let col = 0; col < 9; col++) {
    const set = new Set<string>();
    for (let row = 0; row < 9; row++) {
      const val = board[row][col];
      if (val !== '.') {
        if (set.has(val)) return false;
        else set.add(val);
      }
    }
  }

  return true;
}

export function threeByThreeValid(board: string[][]): boolean {
  for (let sectionRow = 0; sectionRow <= 2; sectionRow++) {
    for (let sectionCol = 0; sectionCol <= 2; sectionCol++) {
      const rowOffset = sectionRow * 3;
      const set = new Set<string>();
      for (let row = 0 + rowOffset; row < 3 + rowOffset; row++) {
        const colOffset = sectionCol * 3;
        for (let col = 0 + colOffset; col < 3 + colOffset; col++) {
          const val = board[row][col];
          if (val !== '.') {
            if (set.has(val)) return false;
            else set.add(val);
          }
        }
      }
    }
  }

  return true;
}
