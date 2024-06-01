/**
 * https://leetcode.com/problems/surrounded-regions/
 */
export { solve };

function solve(board: string[][]): void {
  const ignore = new Set<string>();

  for (let row = 1; row < board.length - 1; row++) {
    for (let col = 1; col < board[0].length - 1; col++) {
      if (board[row][col] === 'O' && !ignore.has(`${row},${col}`)) {
        const connected = connectedSet(board, row, col);
        if (hasBorderingO(board, connected)) {
          for (let c of connected.keys()) {
            ignore.add(c);
          }
        } else {
          for (let c of connected.values()) {
            board[c.row][c.col] = 'X';
          }
        }
      }
    }
  }
}

function hasBorderingO(board: string[][], connected: Map<string, Cell>) {
  const lastRowIndex = board.length - 1;
  const lastColIndex = board[0].length - 1;

  for (let cell of connected.values()) {
    if (
      cell.row === 0 ||
      cell.row === lastRowIndex ||
      cell.col === 0 ||
      cell.col === lastColIndex
    ) {
      return true;
    }
  }

  return false;
}

function connectedSet(board: string[][], row: number, col: number): Map<string, Cell> {
  const lastRowIndex = board.length - 1;
  const lastColIndex = board[0].length - 1;
  const connectedSet = new Map<string, Cell>();

  function dfs(i: number, j: number) {
    if (i < 0 || i > lastRowIndex) return;
    if (j < 0 || j > lastColIndex) return;
    if (board[i][j] === 'X') return;
    let key = `${i},${j}`;
    if (connectedSet.has(key)) return;
    connectedSet.set(`${i},${j}`, { row: i, col: j });
    dfs(i + 1, j);
    dfs(i - 1, j);
    dfs(i, j + 1);
    dfs(i, j - 1);
  }

  dfs(row, col);
  return connectedSet;
}

interface Cell {
  row: number;
  col: number;
}
