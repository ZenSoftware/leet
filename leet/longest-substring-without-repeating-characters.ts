/**
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
 * Given a string s, find the length of the longest substring without repeating characters.
 */

export function lengthOfLongestSubstring(s: string): number {
  if (!s) return 0;

  let longest = 1;

  for (let start = 0; start < s.length - 1; start++) {
    let current = s.charAt(start);

    for (let end = start + 1; end < s.length; end++) {
      const char = s.charAt(end);
      if (!current.includes(char)) {
        current += char;
        if (current.length > longest) {
          longest = current.length;
        }
      } else {
        break;
      }
    }
  }

  return longest;
}
