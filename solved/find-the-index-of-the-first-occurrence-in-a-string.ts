/**
 * https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
 */
export function strStr(haystack: string, needle: string): number {
  for (let i = 0; i < haystack.length; i++) {
    for (let j = 0; j < needle.length; j++) {
      const hayChar = haystack[i + j];
      if (needle[j] !== hayChar) break;
      if (j === needle.length - 1 && needle[j] === hayChar) return i;
    }
  }
  return -1;
}
