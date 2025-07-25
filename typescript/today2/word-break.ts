/**
 * https://leetcode.com/problems/word-break/description/
 */
export { wordBreak };

function wordBreak(s: string, wordDict: string[]): boolean {
  const memo: Record<number, boolean> = {};

  function recurse(sIndex: number): boolean {
    if (sIndex in memo) return memo[sIndex];
    if (sIndex === s.length) return true;

    for (let word of wordDict) {
      let matches = true;
      for (let w = 0; w < word.length; w++) {
        if (s[sIndex + w] !== word[w]) {
          matches = false;
          break;
        }
      }
      if (matches) {
        const result = recurse(sIndex + word.length);
        if (result) return (memo[sIndex] = true);
      }
    }

    return (memo[sIndex] = false);
  }

  return recurse(0);
}
