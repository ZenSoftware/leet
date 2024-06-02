/**
 * https://leetcode.com/problems/word-break/description/
 */
export { wordBreak };

function wordBreak(s: string, wordDict: string[]): boolean {
  function recurse(sIndex: number): boolean {
    if (sIndex === s.length) return true;

    for (let word of wordDict) {
      let matches = true;
      for (let w = 0; w < word.length; w++) {
        if (s[sIndex + w] !== word[w]) {
          matches = false;
          break;
        }
      }
      if (matches) return recurse(sIndex + word.length);
    }

    return false;
  }

  return recurse(0);
}
