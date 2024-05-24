/**
 * https://leetcode.com/problems/longest-palindromic-substring/
 * Given a string s, return the longest palindromic substring in s.
 */
export function longestPalindrome(s: string): string {
  let result = "";
  for (let i = 0; i < s.length - result.length; i++) {
    for (let j = i; j < s.length; j++) {
      const evaluate = s.substring(i, j + 1);
      if (isPalindrome(evaluate)) {
        if (evaluate.length > result.length) {
          result = evaluate;
        }
      }
    }
  }
  return result;
}

export function isPalindrome(s: string) {
  let start = 0;
  let end = s.length - 1;

  while (start < end) {
    if (s[start] !== s[end]) return false;
    start++;
    end--;
  }

  return true;
}
