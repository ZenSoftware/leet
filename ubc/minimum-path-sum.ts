/**
 * https://leetcode.com/problems/minimum-path-sum/
 * [Bottom up approach](https://www.youtube.com/watch?v=pGMsrvt0fpk)
 */
export { minPathSum };

function minPathSum(grid: number[][]): number {
  const solutionRowLength = grid.length + 1;
  const solutionColumnLength = grid[0].length + 1;
  const solution: number[][] = Array(solutionRowLength - 1);
  for (let i = 0; i < solutionRowLength - 1; i++) {
    solution[i] = Array(solutionColumnLength);
  }

  // Fill right most column with infinity
  for (let row = 0; row < solutionRowLength - 1; row++) {
    solution[row][solutionColumnLength - 1] = Infinity;
  }

  // Fill bottom row with infinty
  solution.push(Array(solutionColumnLength - 1).fill(Infinity));

  // Initialize the cell just bellow the last position with 0
  solution[solutionRowLength - 1][solutionColumnLength - 2] = 0;

  for (let col = solutionColumnLength - 2; col >= 0; col--) {
    for (let row = solutionRowLength - 2; row >= 0; row--) {
      const min = Math.min(solution[row + 1][col], solution[row][col + 1]);
      solution[row][col] = grid[row][col] + min;
    }
  }

  return solution[0][0];
}
