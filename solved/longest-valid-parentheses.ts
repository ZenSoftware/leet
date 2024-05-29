/**
 * https://leetcode.com/problems/longest-valid-parentheses/
 * Solution: https://www.youtube.com/watch?v=D5b_JWlkXxw
 */
export function longestValidParentheses(s: string): number {
  let longest = 0;

  let l = 0;
  let r = 0;
  let count = 0;

  for (let i = 0; i < s.length; i++) {
    count++;

    if (s[i] === '(') l++;
    else r++;

    if (l === r) {
      if (count > longest) longest = count;
    } else if (r > l) {
      l = 0;
      r = 0;
      count = 0;
    }
  }

  l = 0;
  r = 0;
  count = 0;

  for (let i = s.length - 1; i >= 0; i--) {
    count++;

    if (s[i] === ')') r++;
    else l++;

    if (l === r) {
      if (count > longest) longest = count;
    } else if (l > r) {
      l = 0;
      r = 0;
      count = 0;
    }
  }

  return longest;
}
