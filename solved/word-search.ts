/**
 * https://leetcode.com/problems/word-search/
 */
export { exist };

function exist(board: string[][], word: string): boolean {
  const lastXIndex = board.length - 1;
  const lastYIndex = board[0].length - 1;

  function dfs(x: number, y: number, remaining: string[]): boolean {
    if (0 > x || x > lastXIndex) return false;
    if (0 > y || y > lastYIndex) return false;
    if (remaining.length === 0) return true;
    if (remaining[0] !== board[x][y]) return false;

    const next = remaining.slice(1);

    const right = dfs(x + 1, y, next);
    if (right) return true;

    const left = dfs(x - 1, y, next);
    if (left) return true;

    const up = dfs(x, y + 1, next);
    if (up) return true;

    const down = dfs(x, y - 1, next);
    if (down) return true;

    return false;
  }

  const characters = word.split('');

  for (let i = 0; i <= lastXIndex; i++) {
    for (let j = 0; j <= lastYIndex; j++) {
      if (dfs(i, j, characters)) return true;
    }
  }

  return false;
}
