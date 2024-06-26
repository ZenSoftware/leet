/**
 * https://leetcode.com/problems/unique-paths/
 */
export { uniquePaths };

function uniquePaths(m: number, n: number): number {
  const memo: Record<string, number> = {};

  function dfs(x: number, y: number) {
    if (x > m || y > n) return 0;
    if (x === m && y === n) return 1;
    const key = `${x},${y}`;
    if (key in memo) return memo[key];

    let total = 0;
    total += dfs(x + 1, y);
    total += dfs(x, y + 1);
    memo[key] = total;
    return total;
  }

  return dfs(1, 1);
}
