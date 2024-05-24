/**
 * https://leetcode.com/problems/longest-palindromic-substring/
 * Given a string s, return the longest palindromic substring in s.
 */
export function longestPalindrome(s: string): string {
  return "";
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
