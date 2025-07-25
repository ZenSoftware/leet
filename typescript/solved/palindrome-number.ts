/**
 * https://leetcode.com/problems/palindrome-number/description/
 * Given an integer x, return true if x is a palindrome, and false otherwise.
 */
export function isPalindrome(x: number): boolean {
  if (x < 0) return false;
  const s = x.toString();
  let start = 0;
  let end = s.length - 1;
  while (start < end) {
    if (s[start] !== s[end]) return false;
    start++;
    end--;
  }
  return true;
}
