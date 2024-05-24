/**
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
 * Given a string s, find the length of the longest substring without repeating characters.
 */

export function lengthOfLongestSubstring(s: string): number {
  if (!s) return 0;

  let longest = 1;

  for (let start = 0; start < s.length - 1; start++) {
    let cache: Record<string, boolean> = { [s.charAt(start)]: true };

    for (let end = start + 1; end < s.length; end++) {
      const char = s.charAt(end);
      if (!cache[char]) {
        cache[char] = true;
        const length = Object.keys(cache).length;
        if (length > longest) {
          longest = length;
        }
      } else {
        break;
      }
    }
  }

  return longest;
}
