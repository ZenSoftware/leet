/**
 * https://leetcode.com/problems/reverse-words-in-a-string/description/
 */
export { reverseWords };

function reverseWords(s: string): string {
  return s.trim().replace(/\s+/g, ' ').split(' ').reverse().join(' ');
}
