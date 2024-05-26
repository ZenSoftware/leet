/**
 *https://leetcode.com/problems/longest-valid-parentheses/
 */
export function longestValidParentheses(s: string): number {
  let longest = 0;

  for (let i = 0; i < s.length - 1; i++) {
    let openCount = 0;
    let charCount = 0;
    for (let j = i; j < s.length; j++) {
      if (s[j] === '(') {
        openCount++;
      } else {
        if (openCount === 0) {
          if (charCount > longest) {
            longest = charCount;
          }
          break;
        }
        openCount--;
      }
      charCount++;
      if (openCount === 0) {
        if (charCount > longest) {
          longest = charCount;
        }
      }
    }
  }

  return longest;
}

export function validParentheses(s: string): boolean {
  let openCount = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === '(') {
      openCount++;
    } else {
      if (openCount === 0) return false;
      openCount--;
    }
  }

  return openCount === 0;
}
