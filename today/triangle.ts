/**
 * https://leetcode.com/problems/triangle/description/
 */
export { minimumTotal };

function minimumTotal(triangle: number[][]): number {
  const memo: Record<string, number> = {};

  function dfs(row: number, col: number): number {
    let key = `${row},${col}`;
    if (key in memo) return memo[key];
    if (row === triangle.length - 1) return triangle[row][col];

    const result1 = triangle[row][col] + dfs(row + 1, col);
    const result2 = triangle[row][col] + dfs(row + 1, col + 1);

    return (memo[key] = Math.min(result1, result2));
  }

  return dfs(0, 0);
}
