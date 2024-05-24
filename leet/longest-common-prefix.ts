/**
 * https://leetcode.com/problems/longest-common-prefix/description/
 */
export function longestCommonPrefix(strs: string[]): string {
  if (strs.length === 0) return "";
  if (strs.length === 1) return strs[0];

  let shortestLength = Infinity;
  for (let s of strs) {
    if (s.length < shortestLength) shortestLength = s.length;
  }

  let result = "";
  for (let i = 0; i < shortestLength; i++) {
    for (let strsIndex = 0; strsIndex < strs.length; strsIndex++) {
      if (strs[0][i] !== strs[strsIndex][i]) {
        return result;
      }
    }
    result += strs[0][i];
  }

  return result;
}
