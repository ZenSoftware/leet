/**
 * https://leetcode.com/problems/word-break/description/
 */
export { wordBreak };

function wordBreak(s: string, wordDict: string[]): boolean {
  const memo: Record<string, boolean> = {};

  function recurse(str: string): boolean {
    if (str in memo) return memo[str];
    if (str.length === 0) return true;

    for (let word of wordDict) {
      let matches = true;
      for (let w = 0; w < word.length; w++) {
        if (str[w] !== word[w]) {
          matches = false;
          break;
        }
      }
      if (matches) {
        const ans = recurse(str.slice(word.length));
        if (ans) return (memo[str] = true);
      }
    }

    return (memo[str] = false);
  }

  return recurse(s);
}
