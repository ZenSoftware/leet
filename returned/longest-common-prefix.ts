/**
 * https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150
 * Write a function to find the longest common prefix string amongst an array of strings.
 * If there is no common prefix, return an empty string "".
 */

export { longestCommonPrefix };

function longestCommonPrefix(strs: string[]): string {
  let result = '';
  let index = 0;

  while (index < strs[0].length) {
    let equals = true;

    for (let i = 1; i < strs.length; i++) {
      if (strs[0][index] !== strs[i][index]) {
        equals = false;
        break;
      }
    }

    if (!equals) break;
    result += strs[0][index++];
  }

  return result;
}
