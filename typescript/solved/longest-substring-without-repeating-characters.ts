/**
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
 *
 * Given a string s, find the length of the longest substring without repeating characters.
 *
 * Solution: [NeetCode - Longest Substring Without Repeating Characters - Leetcode 3 - Python](https://www.youtube.com/watch?v=wiGpQwVHdE0)
 */

export function lengthOfLongestSubstring(s: string): number {
  const set = new Set();
  let index = 0;
  let max = 0;
  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    while (set.has(char)) {
      set.delete(s[index]);
      index++;
    }
    set.add(char);
    max = Math.max(set.size, max);
  }
  return max;
}
