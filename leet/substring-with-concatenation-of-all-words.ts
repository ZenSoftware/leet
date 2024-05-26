/**
 * https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
 */
export function findSubstring(s: string, words: string[]): number[] {
  const perms = permutations(words);
  const permsConcatenated: string[] = [];

  for (let perm of perms) {
    const concatenated = perm.reduce((prev, cur) => prev + cur);
    if (!permsConcatenated.includes(concatenated)) {
      permsConcatenated.push(concatenated);
    }
  }

  const result: number[] = [];

  for (let perm of permsConcatenated) {
    for (let i = 0; i < s.length; i++) {
      for (let j = 0; j < perm.length; j++) {
        if (perm[j] !== s[i + j]) break;
        if (j === perm.length - 1 && perm[j] === s[i + j]) {
          result.push(i);
        }
      }
    }
  }

  return result.sort((a, b) => a - b);
}

export function permutations(words: string[]): string[][] {
  if (words.length === 0) return [[]];

  const first = words[0];
  const withoutFirst = words.slice(1);
  const permsWithoutFirst = permutations(withoutFirst);
  const result: string[][] = [];

  for (let perm of permsWithoutFirst) {
    for (let i = 0; i <= perm.length; i++) {
      result.push([...perm.slice(0, i), first, ...perm.slice(i)]);
    }
  }

  return result;
}
