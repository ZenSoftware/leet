/**
 * https://leetcode.com/problems/unique-paths-ii/
 */
export { uniquePathsWithObstacles };

function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
  const memo: Record<string, number> = {};

  function dfs(x: number, y: number): number {
    const lastX = obstacleGrid.length - 1;
    const lastY = obstacleGrid[0].length - 1;
    if (x > lastX || y > lastY) return 0;
    if (obstacleGrid[x][y] === 1) return 0;
    if (x === lastX && y === lastY) return 1;
    let key = `${x},${y}`;
    if (key in memo) return memo[key];

    let sum = 0;
    sum += dfs(x + 1, y);
    sum += dfs(x, y + 1);

    memo[key] = sum;
    return sum;
  }

  return dfs(0, 0);
}
