/**
 * https://leetcode.com/problems/surrounded-regions/
 */
export { solve };

function solve(board: string[][]): void {
  const lastRowIndex = board.length - 1;
  const lastColIndex = board[0].length - 1;

  for (let y = 0; y <= lastColIndex; y++) {
    if (board[0][y] === 'O') markIgnore(board, 0, y);
    if (board[lastRowIndex][y] === 'O') markIgnore(board, lastRowIndex, y);
  }

  for (let x = 1; x < lastRowIndex; x++) {
    if (board[x][0] === 'O') markIgnore(board, x, 0);
    if (board[x][lastColIndex] === 'O') markIgnore(board, x, lastColIndex);
  }

  for (let x = 0; x <= lastRowIndex; x++) {
    for (let y = 0; y <= lastColIndex; y++) {
      if (board[x][y] === 'O') board[x][y] = 'X';
      if (board[x][y] === 'N') board[x][y] = 'O';
    }
  }
}

function markIgnore(board: string[][], x: number, y: number): void {
  if (board[x]?.[y] !== 'O') return;
  board[x][y] = 'N';
  markIgnore(board, x + 1, y);
  markIgnore(board, x - 1, y);
  markIgnore(board, x, y + 1);
  markIgnore(board, x, y - 1);
}
