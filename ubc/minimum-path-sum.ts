/**
 * https://leetcode.com/problems/minimum-path-sum/
 */
export { minPathSum };

function minPathSum(grid: number[][]): number {
  let minimum = Infinity;
  const lastX = grid.length - 1;
  const lastY = grid[0].length - 1;

  function dfs(x: number, y: number, sum: number) {
    if (x === lastX && y === lastY) {
      minimum = Math.min(minimum, sum + grid[x][y]);
      return;
    }

    if (x + 1 <= lastX) dfs(x + 1, y, sum + grid[x][y]);
    if (y + 1 <= lastY) dfs(x, y + 1, sum + grid[x][y]);
  }

  dfs(0, 0, 0);
  return minimum;
}
