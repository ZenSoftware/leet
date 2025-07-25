/**
 * https://leetcode.com/problems/surrounded-regions/
 */
export { solve };

function solve(board: string[][]): void {
  const lastRow = board.length - 1;
  const lastCol = board[0].length - 1;

  for (let y = 0; y <= lastCol; y++) {
    markIgnore(board, 0, y);
    markIgnore(board, lastRow, y);
  }

  for (let x = 1; x < lastRow; x++) {
    markIgnore(board, x, 0);
    markIgnore(board, x, lastCol);
  }

  for (let x = 0; x <= lastRow; x++) {
    for (let y = 0; y <= lastCol; y++) {
      if (board[x][y] === 'O') board[x][y] = 'X';
      if (board[x][y] === 'I') board[x][y] = 'O';
    }
  }
}

function markIgnore(board: string[][], x: number, y: number): void {
  if (board[x]?.[y] !== 'O') return;
  board[x][y] = 'I';
  markIgnore(board, x + 1, y);
  markIgnore(board, x - 1, y);
  markIgnore(board, x, y + 1);
  markIgnore(board, x, y - 1);
}
