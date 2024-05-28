/**
 * https://leetcode.com/problems/unique-paths/
 */
export { uniquePaths };

function uniquePaths(m: number, n: number): number {
  function dfs(x: number, y: number) {
    if (x > m || y > n) return 0;
    if (x === m && y === n) return 1;

    let total = 0;
    total += dfs(x + 1, y);
    total += dfs(x, y + 1);
    return total;
  }

  return dfs(1, 1);
}
