/**
 * https://leetcode.com/problems/sudoku-solver/description/
 */
export function solveSudoku(board: string[][]): void {
  let cells: Cell[];
  do {
    cells = getCells(board);
    for (let cell of cells) {
      if (cell.unused.size > 1) break;
      const must = cell.unused.values().next();
      board[cell.row][cell.col] = must.value;
    }

    if (cells.length > 0 && cells[0].unused.size > 1) break;
  } while (cells.length);

  console.log(board);
}

function getCells(board: string[][]): Cell[] {
  const unused2D = getUnused2D(board);
  const cells: Cell[] = [];

  for (let row = 0; row < 9; row++) {
    for (let col = 0; col < 9; col++) {
      const unused = unused2D[row][col];
      if (unused !== null) {
        const cell: Cell = { row, col, unused };
        cells.push(cell);
      }
    }
  }

  cells.sort((a, b) => a.unused.size - b.unused.size);
  return cells;
}

function getUnused2D(board: string[][]): (Set<string> | null)[][] {
  // Aggregate the used values for each 3x3 subsection
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

  // Compute the unused values for each cell
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
          if (board[row][col] === '.') {
            unused[row][col] = new Set(['1', '2', '3', '4', '5', '6', '7', '8', '9']);
            for (let usedVal of subSectionUsed[sectionRow][sectionCol]) {
              unused[row][col].delete(usedVal);
            }

            for (let i = 0; i < 9; i++) {
              const val = board[i][col];
              if (val !== '.' && !(rowOffset <= i && i <= rowOffset + 2)) {
                unused[row][col].delete(val);
              }
            }

            for (let j = 0; j < 9; j++) {
              const val = board[row][j];
              if (val !== '.' && !(colOffset <= j && j <= colOffset + 2)) {
                unused[row][col].delete(val);
              }
            }
          }
        }
      }
    }
  }

  return unused;
}

interface Cell {
  row: number;
  col: number;
  unused: Set<string>;
}
