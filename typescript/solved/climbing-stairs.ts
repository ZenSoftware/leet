/**
 * https://leetcode.com/problems/climbing-stairs/
 */
export { climbStairs };

function climbStairs(n: number): number {
  const memo: Record<string, number> = {};

  function dfs(current: number) {
    if (current in memo) return memo[current];
    if (current > n) return 0;
    if (current === n) return 1;

    let total = 0;
    total += dfs(current + 1);
    total += dfs(current + 2);

    memo[current] = total;
    return total;
  }

  return dfs(0);
}
