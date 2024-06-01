/**
 * https://leetcode.com/problems/triangle/description/
 */
export { minimumTotal };

function minimumTotal(triangle: number[][]): number {
  let min = Infinity;

  function dfs(row: number, col: number, sum: number) {
    if (row === triangle.length && sum < min) min = sum;
    if (row >= triangle.length || col >= triangle[row].length) return;

    dfs(row + 1, col, sum + triangle[row][col]);
    dfs(row + 1, col + 1, sum + triangle[row][col]);
  }

  dfs(0, 0, 0);

  return min;
}
