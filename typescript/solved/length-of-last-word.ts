/**
 * https://leetcode.com/problems/length-of-last-word/
 */
export function lengthOfLastWord(s: string): number {
  const trimmed = s.trimEnd();

  for (let i = trimmed.length - 1; i >= 0; i--) {
    if (trimmed[i] === ' ') {
      return trimmed.length - i - 1;
    }
  }

  return trimmed.length;
}
