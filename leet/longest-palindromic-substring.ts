/**
 * https://leetcode.com/problems/longest-palindromic-substring/
 * Given a string s, return the longest palindromic substring in s.
 */
export function longestPalindrome(s: string): string {
  let result = "";
  for (let i = 0; i < s.length - result.length; i++) {
    for (let j = i; j < s.length; j++) {
      let start = i;
      let end = j;
      let isPalindrome = true;

      while (start < end) {
        if (s[start] !== s[end]) {
          isPalindrome = false;
          break;
        }
        start++;
        end--;
      }

      if (isPalindrome) {
        if (j - i + 1 > result.length) {
          result = s.substring(i, j + 1);
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
