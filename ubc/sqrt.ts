/**
 * https://leetcode.com/problems/sqrtx/description/
 */
export { mySqrt };

function mySqrt(x: number): number {
  if (x === 1) return 1;

  let i = 1;

  for (; i < x; i++) {
    if (i * i > x) break;
  }

  return i - 1;
}
