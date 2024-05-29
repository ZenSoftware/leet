/**
 * https://leetcode.com/problems/word-search/
 */
export { exist };

function exist(board: string[][], word: string): boolean {
  const lastXIndex = board.length - 1;
  const lastYIndex = board[0].length - 1;

  function dfs(x: number, y: number, remaining: string[], visited: Set<string>): boolean {
    if (0 > x || x > lastXIndex) return false;
    if (0 > y || y > lastYIndex) return false;
    if (remaining[0] !== board[x][y]) return false;
    if (remaining[0] === board[x][y] && remaining.length === 1) return true;

    const nextRemaining = remaining.slice(1);

    const rightKey = `${x + 1},${y}`;
    if (!visited.has(rightKey)) {
      visited.add(rightKey);
      if (dfs(x + 1, y, nextRemaining, visited)) return true;
      visited.delete(rightKey);
    }

    const leftKey = `${x - 1},${y}`;
    if (!visited.has(leftKey)) {
      visited.add(leftKey);
      if (dfs(x - 1, y, nextRemaining, visited)) return true;
      visited.delete(leftKey);
    }

    const upKey = `${x},${y + 1}`;
    if (!visited.has(upKey)) {
      visited.add(upKey);
      if (dfs(x, y + 1, nextRemaining, visited)) return true;
      visited.delete(upKey);
    }

    const downKey = `${x},${y - 1}`;
    if (!visited.has(downKey)) {
      visited.add(downKey);
      if (dfs(x, y - 1, nextRemaining, visited)) return true;
      visited.delete(downKey);
    }

    return false;
  }

  const boardSize = board.length * board[0].length;
  if (word.length > boardSize) return false;

  const characters = word.split('');

  for (let i = 0; i <= lastXIndex; i++) {
    for (let j = 0; j <= lastYIndex; j++) {
      if (dfs(i, j, characters, new Set())) return true;
    }
  }

  return false;
}
