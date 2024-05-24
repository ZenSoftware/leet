/**
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
 * Given a string s, find the length of the longest substring without repeating characters.
 */

export function lengthOfLongestSubstring(s: string): number {
  if (!s) return 0;

  let longest = 1;
  let current = "";

  for (let start = 0; start < s.length - 1; start++) {
    for (let end = start + 1; end < s.length - longest + 1; end++) {
      const char = s.charAt(end);
      if (!current.includes(char)) {
        current += char;
        if (current.length > longest) {
          longest = current.length;
        }
      }
    }
  }

  return longest;
}
