/**
 * https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150
 * Write a function to find the longest common prefix string amongst an array of strings.
 * If there is no common prefix, return an empty string "".
 */

export { longestCommonPrefix };

function longestCommonPrefix(strs: string[]): string {
  let index = 0;
  const sorted = strs.sort((a, b) => (a < b ? -1 : 1));
  const firstWord = sorted[0];
  const lastWord = sorted[sorted.length - 1];

  for (let i = 0; i < firstWord.length; i++) {
    if (firstWord[i] !== lastWord[i]) {
      break;
    }
    index++;
  }

  return firstWord.slice(0, index);
}
