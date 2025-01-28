/**
 * https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2&envId=top-interview-150
 * Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
 */

export { strStr };

function strStr(haystack: string, needle: string): number {
  for (let h = 0; h <= haystack.length - needle.length; h++) {
    for (let n = 0; n < needle.length; n++) {
      if (haystack[h + n] !== needle[n]) {
        break;
      } else if (n === needle.length - 1) {
        return h;
      }
    }
  }
  return -1;
}
