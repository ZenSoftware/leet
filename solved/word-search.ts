/**
 * https://leetcode.com/problems/word-search/
 */
export { exist };

function exist(board: string[][], word: string): boolean {
  const rowLength = board.length;
  const colLength = board[0].length;

  function backtrack(i: number, j: number, k: number): boolean {
    if (k === word.length) return true;
    if (0 > i || i >= rowLength) return false;
    if (0 > j || j >= colLength) return false;
    if (board[i][j] !== word[k]) return false;

    const temp = board[i][j];
    board[i][j] = '';

    if (backtrack(i + 1, j, k + 1)) return true;
    if (backtrack(i - 1, j, k + 1)) return true;
    if (backtrack(i, j + 1, k + 1)) return true;
    if (backtrack(i, j - 1, k + 1)) return true;

    board[i][j] = temp;
    return false;
  }

  for (let i = 0; i < rowLength; i++) {
    for (let j = 0; j < colLength; j++) {
      if (backtrack(i, j, 0)) return true;
    }
  }

  return false;
}
