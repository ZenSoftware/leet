/**
 * https://leetcode.com/problems/longest-palindromic-substring/
 * Given a string s, return the longest palindromic substring in s.
 */
export function longestPalindrome(s: string): string {
  let result = s[0];

  for (let i = 0; i < s.length; i++) {
    let start = i - 1;
    let end = i + 1;

    while (start >= 0 && end < s.length) {
      if (s[start] !== s[end]) {
        break;
      } else {
        if (end - start + 1 > result.length) {
          result = s.substring(start, end + 1);
        }
      }

      start--;
      end++;
    }

    start = i;
    end = i + 1;

    while (start >= 0 && end < s.length) {
      if (s[start] !== s[end]) {
        break;
      } else {
        if (end - start + 1 > result.length) {
          result = s.substring(start, end + 1);
        }
      }

      start--;
      end++;
    }
  }

  return result;
}
