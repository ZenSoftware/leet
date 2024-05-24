/**
 * https://leetcode.com/problems/reverse-integer/description/
 * Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
 * Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
 */

export function reverse(x: number): number {
  const s = x.toString();
  let result = '';
  if (s[0] === '-') {
    result += '-';
    for (let i = s.length - 1; i >= 1; i--) {
      result += s[i];
    }
  } else {
    for (let i = s.length - 1; i >= 0; i--) {
      result += s[i];
    }
  }
  const intResult = parseInt(result);
  const MAX_INT = 2 ** 31;
  if (intResult < -MAX_INT) return 0;
  if (intResult > MAX_INT - 1) return 0;
  return intResult;
}
