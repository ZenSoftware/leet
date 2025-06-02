/**
 * https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150
 * Given a string s consisting of words and spaces, return the length of the last word in the string.
 * A word is a maximal substring consisting of non-space characters only.
 */

export { lengthOfLastWord };

function lengthOfLastWord(s: string): number {
  let count = 0;
  let i = s.length - 1;

  while (s[i] === ' ') {
    i--;
  }

  while (s[i] !== ' ' && i >= 0) {
    count++;
    i--;
  }

  return count;
}
