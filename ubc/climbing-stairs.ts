/**
 * https://leetcode.com/problems/climbing-stairs/
 */
export { climbStairs };

function climbStairs(n: number): number {
  let result = 0;

  function dfs(current: number) {
    if (current > n) return;
    if (current === n) {
      result++;
      return;
    }
    dfs(current + 1);
    dfs(current + 2);
  }

  dfs(0);
  return result;
}
